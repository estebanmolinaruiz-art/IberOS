// Dependencia cero: simulación espacial de placa/estela con caras, grosor y signos frontales.
// La imagen SVG permanece visible y permite giro táctil incluso si WebGL no existe.
for(const host of document.querySelectorAll(".inscribed-viewer")){
 const svg=host.querySelector(".inscribed-fallback");
 if(!svg)continue;
 const tall=host.dataset.shape==="stele";
 const scene=document.createElement("div");scene.className="stone-3d-scene";
 const stone=document.createElement("div");stone.className="stone-3d-body";
 const front=document.createElement("div");front.className="stone-3d-face stone-3d-front";
 const back=document.createElement("div");back.className="stone-3d-face stone-3d-back";
 const side=document.createElement("div");side.className="stone-3d-face stone-3d-side";
 const top=document.createElement("div");top.className="stone-3d-face stone-3d-top";
 front.append(svg);stone.append(front,back,side,top);scene.append(stone);host.append(scene);
 host.classList.add("stone-3d-ready");host.setAttribute("role","group");host.setAttribute("aria-label","Modelo espacial simbólico giratorio. Arrastra horizontalmente o usa las flechas de giro.");
 const control=document.createElement("div");control.className="stone-3d-controls";
 const left=document.createElement("button"),right=document.createElement("button"),reset=document.createElement("button");
 left.type=right.type=reset.type="button";left.textContent="↶";right.textContent="↷";reset.textContent="Centrar";
 left.setAttribute("aria-label","Girar pieza a la izquierda");right.setAttribute("aria-label","Girar pieza a la derecha");reset.setAttribute("aria-label","Centrar pieza");
 control.append(left,reset,right);host.append(control);
 let x=-7,y=18,startX=0,startY=0,dragging=false;
 function draw(){stone.style.transform="rotateX("+x+"deg) rotateY("+y+"deg)";}draw();
 left.onclick=()=>{y-=25;draw()};right.onclick=()=>{y+=25;draw()};reset.onclick=()=>{x=-7;y=18;draw()};
 scene.addEventListener("pointerdown",e=>{dragging=true;startX=e.clientX;startY=e.clientY;scene.setPointerCapture(e.pointerId)});
 scene.addEventListener("pointermove",e=>{if(!dragging)return;y+=(e.clientX-startX)*.55;x=Math.max(-55,Math.min(55,x-(e.clientY-startY)*.4));startX=e.clientX;startY=e.clientY;draw()});
 for(const event of ["pointerup","pointercancel","lostpointercapture"])scene.addEventListener(event,()=>dragging=false);
}
