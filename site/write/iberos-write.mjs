const DEFAULT_BASE = new URL("./", import.meta.url);
async function loadJSON(url){ const r = await fetch(url); if(!r.ok) throw new Error(`IberOS-Write fetch failed ${r.status}: ${url}`); return r.json(); }
function pct(n,d){ return d ? Math.round((n/d)*1000)/10 : 0; }

export class IberOSWrite {
  constructor({baseUrl}={}){ this.base = new URL(baseUrl || DEFAULT_BASE, document.baseURI); this.rules = null; this.ready = false; }
  async init(){ this.rules = await loadJSON(new URL("data/write-rules.json", this.base)); this.ready = true; return this; }
  info(){ this.#ready(); return structuredClone(this.rules); }
  reconstruct(input){
    this.#ready();
    const text = String(input ?? "").trim();
    if(!text) return this.#abstain(text, ["EMPTY_INPUT"]);
    const normalized = text.toLocaleLowerCase("es-ES").replace(/[¿?¡!.,;:]/g," ").replace(/\s+/g," ").trim();
    const transfer = this.#detectTransferDocument(normalized);
    if(transfer) return this.#renderTransfer(text, transfer);
    return this.#genericAbstention(text);
  }
  #detectTransferDocument(s){
    const hasTransfer = /\b(transfiere|transferir|entrega|entregar)\b/.test(s);
    const hasDocument = /\b(documento|texto|inscripci[oó]n|mensaje)\b/.test(s);
    if(!hasTransfer || !hasDocument) return null;
    let recipient = null;
    if(/\bbastubar\b/i.test(s)) recipient = {surface:"Bastubar", iberian:"BASTUBAR", attested:true};
    else { const m=s.match(/\ba\s+([a-záéíóúüñ][a-záéíóúüñ-]*)\b/i); if(m) recipient={surface:m[1],iberian:null,attested:false}; }
    return {recipient,hasDocument:true};
  }
  #renderTransfer(original,parse){
    const segs=[]; let supported=0,fallback=0,total=4;
    if(parse.recipient?.attested){ segs.push(this.#seg("BASTUBAR-ER","probable","Participante contextual","Antropónimo documentado; -ER contextual.")); supported++; }
    else if(parse.recipient){ const loan=this.#loan(parse.recipient.surface); segs.push(this.#seg(`${loan}-ER`,"fallback","Nombre moderno + relator contextual","Forma moderna marcada como fallback.")); fallback++; supported++; }
    else segs.push(this.#seg("◇RECIPIENT","gap","Participante","No identificado."));
    segs.push(this.#seg("(TE?)","infer","Integración opcional","No se fuerza su presencia.")); supported++;
    segs.push(this.#seg("BI-D(E/I)-ŔOK-(AN)","probable","Complejo verbal de transferencia","No se resuelve DE/DI ni dirección literal de ŔOK.")); supported++;
    segs.push(this.#seg("UTUR","probable","Tema documental/escrito","No se afirma glosa literal exacta.")); supported++;
    return {engine:"IberOS-Write",engine_version:this.rules.version,input:original,intent:"transfer_document_to_person",status:"PARTIAL_RECONSTRUCTION",reconstruction:segs.map(x=>x.form).join(" · "),segments:segs,metrics:{semantic_coverage:pct(supported,total),fallback_rate:pct(fallback,total)},guards:["No word-for-word translation claimed.","DE/DI unresolved.","ŔOK exact direction remains open.","Modern names are fallback unless historically attested."]};
  }
  #genericAbstention(original){ return {engine:"IberOS-Write",engine_version:this.rules.version,input:original,status:"CONTROLLED_ABSTENTION",reconstruction:"◇SEMANTIC_FRAME",segments:[this.#seg("◇SEMANTIC_FRAME","gap","Marco semántico no cubierto","No hay reglas suficientes sin inventar léxico o morfología.")],metrics:{semantic_coverage:0,fallback_rate:0},guards:["No invented Iberian output."]}; }
  #abstain(original,reasons){ return {engine:"IberOS-Write",engine_version:this.rules?.version||"unknown",input:original,status:"CONTROLLED_ABSTENTION",reconstruction:"◇",segments:[],reasons,metrics:{semantic_coverage:0,fallback_rate:0}}; }
  #seg(form,status,role,notes){ return {form,status,role,notes}; }
  #loan(x){ return String(x).normalize("NFD").replace(/[\u0300-\u036f]/g,"").toUpperCase().replace(/[^A-ZÑ-]/g,""); }
  #ready(){ if(!this.ready) throw new Error("Call await write.init() first."); }
}
export async function createIberOSWrite(options={}){ return new IberOSWrite(options).init(); }
