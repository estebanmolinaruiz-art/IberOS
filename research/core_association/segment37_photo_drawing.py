#!/usr/bin/env python3
"""SEGMENT-37: figure inspection and cross-modality photo vs drawing registration.
No sign labels used. Only strong geometric matches can be accepted.
"""
import sys,subprocess,json,hashlib,math
from pathlib import Path
import numpy as np,cv2
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research/core_association/segment37_results"
SRC=ROOT/"research/core_association/segment34_results"
OUT.mkdir(exist_ok=True)
if not all((SRC/f"moleta_fig{i}_candidate_zone.png").exists() for i in (4,5)):
    subprocess.run([sys.executable,str(ROOT/"research/core_association/segment34_moleta_roi.py")],check=True,stdout=subprocess.PIPE)
images={i:cv2.imread(str(SRC/f"moleta_fig{i}_candidate_zone.png"),cv2.IMREAD_GRAYSCALE) for i in (4,5)}
def ascii_repr(im,h=42,w=54):
    a=cv2.resize(im,(w,h),interpolation=cv2.INTER_AREA)
    chars=" .:-=+*#%@"
    lines=["".join(chars[min(9,int(v)*10//256)] for v in row) for row in a]
    return "\n".join(lines)
print("PHOTO FIG4 ASCII\n"+ascii_repr(images[4]))
print("DRAWING FIG5 ASCII\n"+ascii_repr(images[5]))
def features(im,method):
    if method=="SIFT":
        det=cv2.SIFT_create(nfeatures=2500,contrastThreshold=.015,edgeThreshold=12)
    else:
        det=cv2.ORB_create(nfeatures=2500,scaleFactor=1.2,nlevels=8,fastThreshold=8)
    kp,desc=det.detectAndCompute(im,None)
    return kp,desc
def try_align(a,b,method,orientation):
    # Input photo a => drawing b; orientation of drawing may be mirrored/rotated
    oriented={ "identity":b,"flip_x":cv2.flip(b,1),"flip_y":cv2.flip(b,0),
              "rotate180":cv2.rotate(b,cv2.ROTATE_180)}[orientation]
    aa=cv2.createCLAHE(clipLimit=2,tileGridSize=(8,8)).apply(a)
    bb=cv2.createCLAHE(clipLimit=2,tileGridSize=(8,8)).apply(oriented)
    kp1,d1=features(aa,method);kp2,d2=features(bb,method)
    result={"method":method,"orientation":orientation,"photo_features":len(kp1),"drawing_features":len(kp2)}
    if d1 is None or d2 is None or len(d1)<10 or len(d2)<10:
        result["status"]="TOO_FEW_FEATURES";return result
    norm=cv2.NORM_L2 if method=="SIFT" else cv2.NORM_HAMMING
    matcher=cv2.BFMatcher(norm)
    matches=matcher.knnMatch(d1,d2,k=2)
    good=[m for m,n in matches if m.distance <(.7 if method=="SIFT" else .72)*n.distance]
    result["ratio_matches"]=len(good)
    if len(good)<8:
        result["status"]="TOO_FEW_MATCHES";return result
    p1=np.float32([kp1[m.queryIdx].pt for m in good])
    p2=np.float32([kp2[m.trainIdx].pt for m in good])
    H,mask=cv2.findHomography(p1,p2,cv2.RANSAC,4,maxIters=2500,confidence=.995)
    if H is None:
        result["status"]="HOMOGRAPHY_FAILED";return result
    goodmask=mask.ravel().astype(bool)
    src=p1[goodmask];dst=p2[goodmask]
    result["inliers"]=int(goodmask.sum())
    result["inlier_ratio"]=round(float(goodmask.mean()),3)
    result["spatial_coverage_photo"]=round(float(cv2.contourArea(cv2.convexHull(src))/max(a.shape[0]*a.shape[1],1)),3) if len(src)>=3 else 0
    result["spatial_coverage_drawing"]=round(float(cv2.contourArea(cv2.convexHull(dst))/max(b.shape[0]*b.shape[1],1)),3) if len(dst)>=3 else 0
    # Transform sanity; degenerate stretch may produce accidental inliers.
    corners=np.float32([[0,0],[a.shape[1],0],[a.shape[1],a.shape[0]],[0,a.shape[0]]]).reshape(-1,1,2)
    mapped=cv2.perspectiveTransform(corners,H).reshape(-1,2)
    area=abs(cv2.contourArea(mapped.astype(np.float32)))
    result["warp_area_ratio"]=round(float(area/max(b.shape[0]*b.shape[1],1)),3)
    result["H"]=[[round(float(x),7) for x in row] for row in H]
    # Strict: significant inliers, spatial distribution and physically reasonable area.
    result["accepted"]=bool(result["inliers"]>=18 and result["inlier_ratio"]>=.3 and
        result["spatial_coverage_photo"]>=.03 and result["spatial_coverage_drawing"]>=.03 and
        .05<=result["warp_area_ratio"]<=3.5)
    result["status"]="ACCEPTED_GEOMETRIC_TENTATIVE" if result["accepted"] else "REJECTED_GEOMETRIC_GATES"
    return result
results=[]
for method in ("SIFT","ORB"):
    for orientation in ("identity","flip_x","flip_y","rotate180"):
        try:results.append(try_align(images[4],images[5],method,orientation))
        except Exception as exc:results.append({"method":method,"orientation":orientation,"error":str(exc)[:200],"status":"ERROR"})
ranking=sorted(results,key=lambda r:r.get("inliers",0),reverse=True)
report={"protocol":"SEGMENT-37","photo_shape":list(images[4].shape),"drawing_shape":list(images[5].shape),
        "candidates":ranking,"geometric_acceptances":sum(bool(x.get("accepted")) for x in results),
        "independently_verified_glyphs":0,"generalization_confirmed":False,
        "warning":"SIFT/ORB whole-figure registration is not a validated line or sign correspondence; inspect photos and drawings; figures may contain multiple panels."}
(OUT/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
print("REGISTER_RANKINGS",json.dumps([{k:r.get(k) for k in ("method","orientation","ratio_matches","inliers","inlier_ratio","spatial_coverage_photo","spatial_coverage_drawing","warp_area_ratio","status")} for r in ranking],ensure_ascii=False))
