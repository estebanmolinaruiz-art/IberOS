import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createIberOS} from '../site/webengine/iberos-web.mjs';
let checks=0;
globalThis.fetch=async url=>{try{const body=await readFile(fileURLToPath(url));return {ok:true,status:200,text:async()=>body.toString('utf8')}}catch{return {ok:false,status:404,text:async()=>''}}};
function check(value,message){checks++;if(!value)throw Error('FALLA: '+message);console.log('✓ '+message)}
const core=await createIberOS();
const objects=core.loadRegistry();
check(objects.length===38,'Core carga exactamente 38 piezas');
check(new Set(objects.map(x=>x.OBJECT_ID)).size===38,'Identificadores únicos');
check(core.getObject('IBR-CER-0002')?.Nombre_objeto?.includes('Llíria'),'Consulta directa de objeto');
check(core.getObject('NO_EXISTE')===null,'Ausencia de registros falsos');
check(core.search('IBR-CER-0002').some(x=>x.OBJECT_ID==='IBR-CER-0002'),'Búsqueda por identificador');
check(core.search('IBEROS_SIN_COINCIDENCIA_TEST_2026').length===0,'Sin coincidencias es un resultado vacío');
check(core.search('   ').length===0,'Consulta vacía no devuelve inventario entero');
check(core.search('salir').length>0,'Búsqueda sin distinción de mayúsculas');
check(core.listFamilies().length>0,'Familias cargadas');
check(core.familyObjects(core.listFamilies()[0]).length>0,'Relaciones con objetos reales');
console.log('Core: '+checks+' pruebas funcionales superadas');