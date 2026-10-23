const DEFAULT_BASE = new URL("./", import.meta.url);
async function loadJSON(url){ const r = await fetch(url); if(!r.ok) throw new Error(`IberOS-Write fetch failed ${r.status}: ${url}`); return r.json(); }
function pct(n,d){ return d ? Math.round((n/d)*1000)/10 : 0; }

export class IberOSWrite {
  constructor({baseUrl}={}){ this.base = new URL(baseUrl || DEFAULT_BASE, document.baseURI); this.rules = null; this.ready = false; }
  async init(){ this.rules = await loadJSON(new URL("data/write-rules.json", this.base)); this.ready = true; return this; }
  info(){ this.#ready(); return structuredClone(this.rules); }
  phonographicFallback(input){
    this.#ready();
    const source=String(input??"").trim();
    const normalized=source.toLocaleLowerCase("es-ES").normalize("NFD").replace(/[\u0300-\u036f]/g,"").normalize("NFC");
    const words=normalized.split(/\s+/u).filter(Boolean);
    const warnings=[];
    const encodedWords=words.map(word=>this.#encodeSpanishWord(word,warnings)).filter(x=>x.tokens.length);
    return {
      mode:"WRITE_FALLBACK_PHONOGRAPHIC",
      source_language:"es",
      source_text:source,
      semantic_translation:false,
      script_system:"northeastern_iberian_conventional_modern_mapping",
      words:encodedWords,
      tokens:encodedWords.flatMap((x,i)=>i?[{value:"·",kind:"separator"},...x.tokens]:x.tokens),
      warnings:[...new Set(warnings)],
      label:"Transliteración moderna aproximada; no traducción ibérica."
    };
  }
  decodeGeneratedFallback(fallback){
    this.#ready();
    if(!fallback || fallback.mode!=="WRITE_FALLBACK_PHONOGRAPHIC"){
      return {status:"NOT_REVERSIBLE",exact:false,spanish:null,reason:"La entrada no es una salida fonográfica generada por IberOS-Write."};
    }
    const spanish=String(fallback.source_text??"").trim();
    if(!spanish){
      return {status:"NOT_REVERSIBLE",exact:false,spanish:null,reason:"La salida no conserva texto fuente."};
    }
    return {
      status:"EXACT_SOURCE_RECOVERY",
      exact:true,
      spanish,
      method:"stored_source_trace",
      warning:"Recuperación exacta del castellano fuente conservado por Write; no desciframiento de una inscripción antigua."
    };
  }
  reconstruct(input){
    this.#ready();
    const text = String(input ?? "").trim();
    if(!text) return this.#abstain(text, ["EMPTY_INPUT"]);
    const normalized = text.toLocaleLowerCase("es-ES").replace(/\.$/,"").replace(/\s+/g," ").trim();
    const transfer = this.#detectTransferDocument(normalized);
    if(transfer) return this.#renderTransfer(text, transfer);
    return this.#genericAbstention(text);
  }
  #detectTransferDocument(s){
    // Full affirmative passive frames only. Keyword co-occurrence cannot fix roles.
    const name = "([\\p{L}][\\p{L}\\p{M}-]*)";
    const action = "se (?:transfiere|entrega) (?:un (?:documento|texto|mensaje)|una inscripci[oó]n)";
    const front = s.match(new RegExp(`^a ${name} ${action}$`,"u"));
    const end = s.match(new RegExp(`^${action} a ${name}$`,"u"));
    const unnamed = new RegExp(`^${action}$`,"u").test(s);
    if(!front && !end && !unnamed) return null;
    const surface = front?.[1] || end?.[1];
    const unresolvedParticipants = new Set(["nadie","ninguno","ninguna","todos","todas","alguien","quién","quien","qué","que","cuál","cual","él","el","ella","ellos","ellas","mí","mi","ti","nosotros","nosotras","vosotros","vosotras","usted","ustedes","no"]);
    if(surface && unresolvedParticipants.has(surface)) return null;
    let recipient = null;
    if(surface === "bastubar") recipient = {surface:"Bastubar", iberian:"BASTUBAR", attested:true};
    else if(surface) recipient = {surface,iberian:null,attested:false};
    return {recipient,hasDocument:true};
  }
  #renderTransfer(original,parse){
    const segs=[];
    if(parse.recipient?.attested){ segs.push(this.#seg("BASTUBAR-ER","probable","Participante contextual","Antropónimo documentado; -ER contextual.")); }
    else if(parse.recipient){ const loan=this.#loan(parse.recipient.surface); segs.push(this.#seg(`${loan}-ER`,"fallback","Nombre moderno + relator contextual","Forma moderna marcada como fallback.")); }
    else segs.push(this.#seg("◇RECIPIENT","gap","Participante","No identificado."));
    segs.push(this.#seg("(TE?)","infer","Integración opcional","No se fuerza su presencia."));
    segs.push(this.#seg("BI-D(E/I)-ŔOK-(AN)","structural","Complejo verbal de transferencia","No se resuelve DE/DI ni dirección literal de ŔOK."));
    segs.push(this.#seg("UTUR","probable","Tema documental/escrito","No se afirma glosa literal exacta."));
    return {engine:"IberOS-Write",engine_version:this.rules.version,input:original,intent:"transfer_document_to_person",status:"PARTIAL_RECONSTRUCTION",reconstruction:segs.map(x=>x.form).join(" · "),segments:segs,metrics:this.#metrics(segs),guards:["No word-for-word translation claimed.","DE/DI unresolved.","ŔOK exact direction remains open.","Modern names are fallback unless historically attested."]};
  }
  #genericAbstention(original){ const fallback=this.phonographicFallback(original); return {engine:"IberOS-Write",engine_version:this.rules.version,input:original,status:"CONTROLLED_ABSTENTION",reconstruction:"◇SEMANTIC_FRAME",segments:[this.#seg("◇SEMANTIC_FRAME","gap","Marco semántico no cubierto","No hay reglas suficientes sin inventar léxico o morfología.")],fallback,metrics:this.#metrics([{status:"gap"}]),guards:["No invented Iberian semantic output.","Fallback is a modern phonographic representation, not a historical translation."]}; }
  #abstain(original,reasons){ return {engine:"IberOS-Write",engine_version:this.rules?.version||"unknown",input:original,status:"CONTROLLED_ABSTENTION",reconstruction:"◇",segments:[],reasons,metrics:this.#metrics([])}; }
  #encodeSpanishWord(raw,warnings){
    const word=String(raw).replace(/[^a-zñü]/gu,"");
    const tokens=[];
    const vowels=new Set(["a","e","i","o","u"]);
    const push=(value,source,kind="sign")=>tokens.push({value,source,kind});
    for(let i=0;i<word.length;){
      let c=word[i],n=word[i+1]||"",n2=word[i+2]||"";
      if(c==="h"){warnings.push("H castellana omitida por carecer de correspondencia fonética directa.");i++;continue;}
      if(c==="ü"){push("u","ü");i++;continue;}
      if(vowels.has(c)){push(c,c);i++;continue;}
      if(c==="r"&&n==="r"){push("ŕ","rr");i+=2;continue;}
      if(c==="c"&&(n==="e"||n==="i")){push("s","c");i++;continue;}
      if(c==="z"){push("s","z");i++;continue;}
      if(c==="q"&&n==="u"&&(n2==="e"||n2==="i")){push("k"+n2,"qu"+n2);i+=3;continue;}
      if(c==="g"&&n==="u"&&(n2==="e"||n2==="i")){push("k"+n2,"gu"+n2);i+=3;warnings.push("G/QU se normalizan a la serie velar como aproximación moderna.");continue;}
      if((c==="b"||c==="v"||c==="p")&&vowels.has(n)){push("b"+n,c+n);i+=2;if(c!=="b")warnings.push("P/V se aproximan a la serie labial ibérica.");continue;}
      if((c==="t"||c==="d")&&vowels.has(n)){push("t"+n,c+n);i+=2;if(c==="d")warnings.push("D se aproxima a la serie dental ibérica.");continue;}
      if((c==="k"||c==="g")&&vowels.has(n)){push("k"+n,c+n);i+=2;if(c==="g")warnings.push("G se aproxima a la serie velar ibérica.");continue;}
      if(c==="c"&&vowels.has(n)){push("k"+n,c+n);i+=2;continue;}
      if(["l","m","n","r","s"].includes(c)){push(c,c);i++;continue;}
      if(c==="ñ"){push("n","ñ");warnings.push("Ñ se aproxima a N en este fallback moderno.");i++;continue;}
      if(c==="x"){push("k","x");push("s","x");warnings.push("X se descompone aproximadamente como K+S.");i++;continue;}
      if(c==="j"||(c==="g"&&(n==="e"||n==="i"))||c==="f"||c==="y"||c==="w"){
        push("◇",c,"gap");warnings.push("Hay sonidos castellanos sin correspondencia ibérica segura; se muestran como hueco.");i++;continue;
      }
      warnings.push("Se omitió un carácter sin regla fonográfica: "+c);i++;
    }
    return {source:raw,tokens};
  }
  #metrics(segments){
    const count=status=>segments.filter(s=>s.status===status).length;
    const total=segments.length;
    return {
      semantic_coverage:pct(count("validated"),total),
      probable_rate:pct(count("probable"),total),
      structural_rate:pct(count("structural"),total),
      infer_rate:pct(count("infer"),total),
      fallback_rate:pct(count("fallback"),total),
      gap_rate:pct(count("gap"),total),
      total_segments:total,
      coverage_basis:"validated_semantic_segments_only",
      official_metrics_changed:false,
    };
  }
  #seg(form,status,role,notes){ return {form,status,role,notes}; }
  #loan(x){ return String(x).normalize("NFD").replace(/[\u0300-\u036f]/g,"").toUpperCase().replace(/[^A-ZÑ-]/g,""); }
  #ready(){ if(!this.ready) throw new Error("Call await write.init() first."); }
}
export async function createIberOSWrite(options={}){ return new IberOSWrite(options).init(); }
