export async function text(url){const r=await fetch(url);if(!r.ok)throw new Error(url+" · HTTP "+r.status);return r.text()}
export function csv(s){s=s.replace(/^\uFEFF/,"");const rows=[];let r=[],f="",q=false;for(let i=0;i<s.length;i++){const c=s[i];if(q){if(c==='"'&&s[i+1]==='"'){f+='"';i++}else if(c==='"')q=false;else f+=c}else if(c==='"')q=true;else if(c===','){r.push(f);f=""}else if(c==='\n'){r.push(f.replace(/\r$/,""));rows.push(r);r=[];f=""}else f+=c}if(f||r.length){r.push(f);rows.push(r)}const h=rows.shift()||[];return rows.filter(x=>x.some(Boolean)).map(x=>Object.fromEntries(h.map((k,i)=>[k,x[i]??""])))}
export const esc=s=>String(s??"").replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[m]));
export const tags=s=>String(s||"").split(";").map(x=>x.trim()).filter(Boolean);
export function header(prefix="../"){
 const p=location.pathname;
 const active=k=>p.includes(k)?" active":"";
 const home=(p.endsWith("/IberOS/")||p.endsWith("/IberOS/index.html"))?"active":"";
 queueMicrotask(()=>{const b=document.querySelector(".menu-toggle"),n=document.querySelector(".main-nav");if(b&&n&&!b.dataset.bound){b.dataset.bound="1";b.addEventListener("click",()=>n.classList.toggle("open"));}});
 return '<header class="site-header"><div class="header-inner">'+
 '<a class="brand" href="'+prefix+'"><span class="brand-mark">IB</span><span class="brand-text"><strong>Iber<span>OS+</span></strong><small>Datos · inteligencia artificial · epigrafía ibérica</small></span></a>'+
 '<button class="menu-toggle" aria-label="Abrir menú">☰</button>'+
 '<nav class="main-nav"><a class="'+home+'" href="'+prefix+'">Inicio</a><a class="'+active("/corpus/")+'" href="'+prefix+'corpus/">Corpus</a><a class="'+active("/herramientas/")+'" href="'+prefix+'herramientas/">Herramientas</a><a class="'+active("/comunidad/")+'" href="'+prefix+'comunidad/">Comunidad</a><a class="'+active("/recursos/")+'" href="'+prefix+'recursos/">Recursos</a><a class="'+active("/acerca/")+'" href="'+prefix+'acerca/">Acerca de</a></nav>'+
 '<div class="nav-actions"><a class="nav-search" href="'+prefix+'corpus/" aria-label="Buscar en el corpus">⌕</a><a class="nav-cta" href="'+prefix+'laboratorio/">Iniciar proyecto</a></div></div></header>';
}