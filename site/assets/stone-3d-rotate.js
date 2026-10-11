// IberOS symbolic stone mesh rendered in 2D Canvas: no WebGL/CDN.
// The irregular stone's front, sides and glyphs transform together in 3D.
const glyphs=[
[[[-.72,.48],[-.52,.82],[-.31,.48]], [[-.52,.82],[-.52,.28]]],
[[[-.15,.73],[-.15,.25]], [[-.15,.50],[.03,.69]]],
[[[.23,.72],[.50,.31],[.73,.72]],[[.50,.31],[.50,.16]]],
[[[-.65,-.12],[-.36,-.49],[-.12,-.11]], [[-.36,-.49],[-.36,-.71]]],
[[[.17,-.16],[.45,-.54],[.73,-.16]],[[.17,-.54],[.73,-.54]]]
];
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
for(const host of document.querySelectorAll(".inscribed-viewer")){
 const original=host.querySelector(".inscribed-fallback");
 if(!original)continue;
 const tall=host.dataset.shape==="stele";
 const canvas=document.createElement("canvas");canvas.className="stone-mesh-canvas";
 canvas.setAttribute("role","img");canvas.setAttribute("aria-label","Piedra tridimensional simbólica de forma irregular con signos en su cara frontal");
 const controls=document.createElement("div");controls.className="stone-mesh-controls";
 const buttons=[["↶","Girar a la izquierda"],["Centrar","Centrar piedra"],["↷","Girar a la derecha"]];
 const cs=buttons.map(([label,aria])=>{const b=document.createElement("button");b.type="button";b.textContent=label;b.setAttribute("aria-label",aria);controls.append(b);return b});
 let yaw=.28,pitch=-.16,drag=false,sx=0,sy=0;
 const polygon=tall?[[-.71,1.2],[-.44,1.42],[.33,1.39],[.63,1.12],[.69,-1.20],[.34,-1.44],[-.59,-1.38],[-.75,-1.13]]:[[-1.45,.74],[-1.06,1.02],[.74,.98],[1.43,.72],[1.47,-.65],[1.02,-.96],[-1.23,-.86],[-1.55,-.52]];
 const P=polygon.map(([x,y])=>[x,y,.18]),B=polygon.map(([x,y])=>[x,y,-.19]);
 const rotate=([x,y,z])=>{const cy=Math.cos(yaw),sy=Math.sin(yaw),cx=Math.cos(pitch),sx=Math.sin(pitch);const nx=x*cy+z*sy,nz=z*cy-x*sy;return [nx,y*cx-nz*sx,y*sx+nz*cx]};
 function draw(){
   const w=host.clientWidth||350,h=host.clientHeight||330,dpr=Math.min(devicePixelRatio||1,2);
   canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);
   const ctx=canvas.getContext("2d");if(!ctx)return;ctx.scale(dpr,dpr);
   const bg=ctx.createRadialGradient(w*.45,h*.3,10,w*.5,h*.48,w*.65);bg.addColorStop(0,"#506773");bg.addColorStop(1,"#1b3441");ctx.fillStyle=bg;ctx.fillRect(0,0,w,h);
   const scale=Math.min(w/(tall?4.6:4.4),(h-58)/(tall?4.5:3.5))*1.14,centerY=(h-45)/2;
   const proj=pt=>{let [x,y,z]=rotate(pt);let k=5.5/(5.5-z);return [w/2+x*scale*k,centerY-y*scale*k,z]};
   const trace=pts=>{ctx.beginPath();pts.forEach((p,i)=>{const [x,y]=proj(p);i?ctx.lineTo(x,y):ctx.moveTo(x,y)});ctx.closePath()};
   const faces=[];
   for(let i=0;i<P.length;i++){let j=(i+1)%P.length;const ps=[P[i],P[j],B[j],B[i]];faces.push({ps,depth:ps.reduce((a,p)=>a+rotate(p)[2],0)/4,col:i%2?"#807058":"#9a8567"})}
   faces.push({ps:B,depth:B.reduce((a,p)=>a+rotate(p)[2],0)/B.length,col:"#675b49",back:true});
   faces.push({ps:P,depth:P.reduce((a,p)=>a+rotate(p)[2],0)/P.length,col:"#b2a080",front:true});
   faces.sort((a,b)=>a.depth-b.depth);
   for(const f of faces){trace(f.ps);ctx.fillStyle=f.col;ctx.fill();ctx.strokeStyle="#d0b991";ctx.lineWidth=1.1;ctx.stroke();
    if(f.front){
      ctx.save();trace(P);ctx.clip();
      const strokes=tall?glyphs.slice(0,4):glyphs;
      strokes.forEach((paths,i)=>{for(const path of paths){ctx.beginPath();path.forEach(([gx,gy],k)=>{let x=tall?gx*.77:(gx*.86),y=tall?gy*.66+(.56-i*.37):gy;const q=proj([x,y,.201]);k?ctx.lineTo(q[0],q[1]):ctx.moveTo(q[0],q[1])});ctx.strokeStyle="#46382a";ctx.lineCap="round";ctx.lineJoin="round";ctx.lineWidth=clamp(scale*.08,3,8);ctx.stroke()}});
      ctx.restore();
    }
   }
 }
 function update(){requestAnimationFrame(draw)}
 host.replaceChildren(canvas,controls);host.classList.add("stone-mesh-ready");
 cs[0].onclick=()=>{yaw-=Math.PI/8;update()};cs[1].onclick=()=>{yaw=.28;pitch=-.16;update()};cs[2].onclick=()=>{yaw+=Math.PI/8;update()};
 canvas.style.touchAction="none";
 canvas.addEventListener("pointerdown",e=>{drag=true;sx=e.clientX;sy=e.clientY;canvas.setPointerCapture(e.pointerId)});
 canvas.addEventListener("pointermove",e=>{if(!drag)return;yaw+=(e.clientX-sx)*.012;pitch=clamp(pitch+(e.clientY-sy)*.009,-1.3,1.3);sx=e.clientX;sy=e.clientY;update()});
 for(const ev of ["pointerup","pointercancel","lostpointercapture"])canvas.addEventListener(ev,()=>drag=false);
 new ResizeObserver(update).observe(host);update();
}
