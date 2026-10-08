const DEFAULT_REMOTE = 'https://raw.githubusercontent.com/estebanmolinaruiz-art/IberOS/main/';

function csvParse(text) {
  const rows = [];
  let row = [], field = '', q = false;
  const pushField = () => { row.push(field); field = ''; };
  const pushRow = () => { rows.push(row); row = []; };
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) {
      if (c === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (c === '"') q = false;
      else field += c;
    } else {
      if (c === '"') q = true;
      else if (c === ',') pushField();
      else if (c === '\n') { pushField(); pushRow(); }
      else if (c !== '\r') field += c;
    }
  }
  if (field.length || row.length) { pushField(); pushRow(); }
  if (!rows.length) return [];
  const headers = rows.shift().map((h, i) => i === 0 ? h.replace(/^\uFEFF/, '') : h);
  return rows.filter(r => r.some(v => v !== '')).map(r => Object.fromEntries(headers.map((h, i) => [h, r[i] ?? ''])));
}

async function fetchText(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`IberOS fetch failed ${r.status}: ${url}`);
  return r.text();
}
async function fetchJSON(url) { return JSON.parse(await fetchText(url)); }
function splitFamilies(v='') { return String(v).split(';').map(x=>x.trim()).filter(Boolean); }

export class IberOSWeb {
  constructor(options={}) {
    this.remoteBase = options.remoteBase || DEFAULT_REMOTE;
    this.objects = [];
    this.familyLinks = [];
    this.schema = null;
    this.ready = false;
  }
  _remote(path){ return new URL(path, this.remoteBase).href; }
  async _load(path, type='text') { return type === 'json' ? fetchJSON(this._remote(path)) : fetchText(this._remote(path)); }
  async init() {
    const [registryCSV, familyCSV, schema] = await Promise.all([
      this._load('src/iberos/data/iberos_objects_registry_v2.0.csv'),
      this._load('src/iberos/data/iberos_family_links_v2.0.csv'),
      this._load('src/iberos/schema/iberos-result-v1.schema.json','json')
    ]);
    this.objects = csvParse(registryCSV);
    this.familyLinks = csvParse(familyCSV);
    this.schema = schema;
    this.ready = true;
    return this;
  }
  _assert(){ if(!this.ready) throw new Error('Call await engine.init() before using IberOSWeb.'); }
  loadRegistry(){ this._assert(); return structuredClone(this.objects); }
  getObject(objectId){ this._assert(); const x=this.objects.find(r=>r.OBJECT_ID===objectId); return x?structuredClone(x):null; }
  familyObjects(family){ this._assert(); const key=String(family).toUpperCase(); return this.objects.filter(r=>splitFamilies(r.Familias_Tags).some(x=>x.toUpperCase()===key)).map(structuredClone); }
  listFamilies(){ this._assert(); const s=new Set(); this.objects.forEach(r=>splitFamilies(r.Familias_Tags).forEach(f=>s.add(f))); return [...s].sort(); }
  search(query){
    this._assert(); const q=String(query??'').trim().toLowerCase(); if(!q) return [];
    const fields=['OBJECT_ID','Referencia_epigráfica','Nombre_objeto','Yacimiento','Localidad','Soporte','Escritura','Familias_Tags','Observaciones'];
    return this.objects.filter(r=>fields.some(k=>String(r[k]??'').toLowerCase().includes(q))).map(structuredClone);
  }
}
export async function createIberOS(options={}) { return new IberOSWeb(options).init(); }
export const IBEROS_WEB_ENGINE_VERSION = '1.0.1-web.2';
