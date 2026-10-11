/* Navigation context only. No claim that a source object was analyzed automatically. */
export function showResearchContext(){
 const params=new URLSearchParams(location.search);const id=params.get("id")||(location.pathname.includes("/webengine/")?params.get("q"):null);
 if(!id||!/^[A-Z0-9-]{4,60}$/.test(id))return;
 const main=document.querySelector("main");if(!main)return;
 const bar=document.createElement("nav");bar.className="research-context";bar.setAttribute("aria-label","Recorrido de investigación");
 const label=document.createElement("strong");label.textContent="Pieza seleccionada: "+id;bar.append(label);
 const links=[["Ficha","ficha/?id="],["Core","webengine/?q="],["Write","write/?id="],["Talk","talk/?id="],["Laboratorio","laboratorio/?id="]];
 for(const [name,dest] of links){const a=document.createElement("a");a.textContent=name;a.href="../"+dest+encodeURIComponent(id);if(location.pathname.includes("/"+dest.split("/")[0]+"/"))a.setAttribute("aria-current","page");bar.append(a)}
 const note=document.createElement("small");note.textContent="Navegación contextual: abrir Write o Talk no implica analizar automáticamente esta pieza.";bar.append(note);
 main.prepend(bar);
}
