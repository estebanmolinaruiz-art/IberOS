/** Shared CORE audit status for browser/mobile Write and Talk interfaces. */
export async function loadMobileCoreStatus(url="../data/mobile_core_bundle_v1.json", fetcher=fetch) {
  const response=await fetcher(url);
  if(!response.ok)throw new Error("CORE bundle HTTP "+response.status);
  const payload=await response.json();
  if(payload.schema!=="IberOS-Mobile-Bundle/1.0" ||
     payload.object_count!==38 ||
     Object.keys(payload.objects||{}).length!==38 ||
     Object.values(payload.objects).some(o=>o.automatic_core_promotion!==false||o.translation_validated!==false))
    throw new Error("CORE bundle invalid or scientifically unsafe");
  return {schema:payload.schema,object_count:payload.object_count,
          authority:payload.authority,scientific_state:"UNVERIFIED"};
}
export async function showMobileCoreStatus(element,url="../data/mobile_core_bundle_v1.json",fetcher=fetch) {
  try {
    const state=await loadMobileCoreStatus(url,fetcher);
    if(element)element.textContent="CORE sincronizado · "+state.object_count+
      " fichas · C594/C474 · sin traducciones automáticas validadas";
    return state;
  }catch(error){
    if(element)element.textContent="CORE móvil no disponible: funcionan las herramientas locales, sin datos sincronizados.";
    return null;
  }
}
