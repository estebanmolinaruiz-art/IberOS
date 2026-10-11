import * as THREE from "https://esm.sh/three@0.161.0";
const paths=[
 [[0,1],[.5,0],[1,1],[.5,1],[.5,0]],
 [[0,0],[1,0],[.5,.5],[1,1],[0,1]],
 [[.5,0],[.5,1],[0,.65],[1,.65]],
 [[0,0],[1,1],[1,0],[0,1]],
 [[0,0],[0,1],[1,1],[1,0],[0,.5],[1,.5]],
 [[.5,0],[0,.5],[.5,1],[1,.5],[.5,0]],
 [[0,0],[1,0],[.5,1],[.5,0]],
 [[0,0],[1,0],[0,1],[1,1]]
];
function stoneTexture(tall){
 const c=document.createElement("canvas");c.width=768;c.height=768;
 const ctx=c.getContext("2d"),w=c.width,h=c.height;
 ctx.fillStyle=tall?"#95826a":"#a9987b";ctx.fillRect(0,0,w,h);
 for(let i=0;i<5200;i++){const x=(i*173)%w,y=(i*271+Math.floor(i/11)*97)%h;ctx.fillStyle=i%3?"rgba(31,25,18,.05)":"rgba(255,235,197,.07)";ctx.fillRect(x,y,(i%7)+1,(i%5)+1)}
 ctx.strokeStyle="rgba(60,43,29,.72)";ctx.lineCap="round";ctx.lineJoin="round";ctx.lineWidth=10;
 const glyphs=tall?[0,5,2,4,7,1]:[3,0,6,2,5,1,4,7];
 glyphs.forEach((n,i)=>{const cols=tall?3:4,stepX=tall?165:155,stepY=tall?250:230;
 const ox=(tall?120:75)+(i%cols)*stepX,oy=(tall?140:180)+Math.floor(i/cols)*stepY;
 ctx.beginPath();paths[n].forEach(([x,y],j)=>{const X=ox+x*73,Y=oy+y*105;j?ctx.lineTo(X,Y):ctx.moveTo(X,Y)});ctx.stroke();
 ctx.strokeStyle="rgba(221,195,150,.27)";ctx.lineWidth=3;ctx.stroke();ctx.strokeStyle="rgba(60,43,29,.72)";ctx.lineWidth=10;
 });
 return new THREE.CanvasTexture(c);
}
function renderPiece(el){
 const tall=el.dataset.shape==="stele",scene=new THREE.Scene();scene.background=new THREE.Color("#203543");
 const camera=new THREE.PerspectiveCamera(40,1,.1,50);camera.position.set(0,.1,tall?5.7:5.3);
 const renderer=new THREE.WebGLRenderer({antialias:true,alpha:false});renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));renderer.outputColorSpace=THREE.SRGBColorSpace;
 el.replaceChildren(renderer.domElement);renderer.domElement.setAttribute("aria-label",tall?"Estela 3D con signos gráficos ilustrativos":"Placa 3D con signos gráficos ilustrativos");
 const group=new THREE.Group();scene.add(group);
 const width=tall?2.25:3.4,height=tall?3.3:2.25,depth=.25;
 const rock=new THREE.Mesh(new THREE.BoxGeometry(width,height,depth),new THREE.MeshStandardMaterial({color:"#9e8b72",roughness:1}));group.add(rock);
 const face=new THREE.Mesh(new THREE.PlaneGeometry(width-.08,height-.08),new THREE.MeshStandardMaterial({map:stoneTexture(tall),roughness:1,side:THREE.FrontSide}));face.position.z=depth/2+.004;group.add(face);
 group.rotation.set(-.12,.27,.03);scene.add(new THREE.HemisphereLight(0xf7e6bd,0x344757,2));const light=new THREE.DirectionalLight(0xffedc9,2.1);light.position.set(-3,5,7);scene.add(light);
 let held=false,lastX=0,lastY=0;
 el.addEventListener("pointerdown",e=>{held=true;lastX=e.clientX;lastY=e.clientY;el.setPointerCapture(e.pointerId)});
 el.addEventListener("pointermove",e=>{if(!held)return;group.rotation.y+=(e.clientX-lastX)*.009;group.rotation.x+=(e.clientY-lastY)*.008;lastX=e.clientX;lastY=e.clientY});
 el.addEventListener("pointerup",()=>held=false);el.addEventListener("pointercancel",()=>held=false);
 const resize=()=>{const w=el.clientWidth,h=el.clientHeight;if(w<2||h<2)return;camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h,false)};resize();new ResizeObserver(resize).observe(el);
 let live=true;const frame=()=>{if(!live)return;renderer.render(scene,camera);requestAnimationFrame(frame)};frame();
 window.addEventListener("pagehide",()=>{live=false;renderer.dispose()},{once:true});
}
for(const el of document.querySelectorAll(".inscribed-viewer")){try{renderPiece(el)}catch(e){el.textContent="No se ha podido iniciar el visor 3D: "+e.message}}
