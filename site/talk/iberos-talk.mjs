export const AUTHORITY = Object.freeze({semantic_release:"C594",prospective_lock:"C474",technical_floor:"C539",rok_network:"C541"});
export const VERSION = "TALK-WEB v0.2-guarded";
const entries = [
  {form:"BAIDES",family:"BAIDES_BAITES"},{form:"BAITES",family:"BAIDES_BAITES"},
  {form:"BATIR",family:"BATIR_FAMILY"},{form:"EBANEN",family:"EBANEN_FORMULA"},
  {form:"EKIAR",family:"KIAR_FAMILY"},{form:"IUNSTIR",family:"IUNSTIR_FORMULA"},
  {form:"KIAR",family:"KIAR_FAMILY"},{form:"KUTUI",family:"KUTU_EXTERNAL"},
  {form:"KUTUKA",family:"KUTU_EXTERNAL"},{form:"KUTUR",family:"KUTUR_FAMILY"},
  {form:"ROK",family:"ROK_NETWORK"},{form:"SALIR",family:"SALIR_FAMILY"},
];
const byForm = new Map(entries.map(entry=>[entry.form,entry]));

export function analyzeTalk(input){
  const tokens=String(input??"").trim().split(/\s+/u).filter(Boolean).map(raw=>{
    const form=raw.normalize("NFC").toUpperCase();
    const plain=/^[A-ZŔŚ]+$/u.test(form);
    const entry=plain?byForm.get(form):null;
    const state=!plain?"BLOCKED_NOTATION":form==="SETEBANE"?"BLOCKED_ENTRY":entry?"DOCUMENTED_FORM_UNREVIEWED":"UNRECOGNIZED_FORM";
    return {raw,form,state,family:entry?.family??null,category:"UNKNOWN",meaning_status:"UNRESOLVED",demo_eligible:!!entry,production_whole_word_ready:false,historical_pronunciation_validated:false};
  });
  return {engine:"IberOS-Talk",version:VERSION,authority:{...AUTHORITY},tokens,approved_whole_words:0,official_metrics_changed:false};
}

export function prepareSyntheticPlayback(input){
  const analysis=analyzeTalk(input);
  const allowed=analysis.tokens.length>0&&analysis.tokens.every(token=>token.demo_eligible);
  return {allowed,text:allowed?analysis.tokens.map(token=>token.form.toLowerCase()).join(" "):null,mode:"BROWSER_SYNTHESIS_DEMO_ONLY",reason:allowed?null:analysis.tokens.length?"UNRESOLVED_OR_NONLEXICAL_INPUT":"EMPTY_INPUT",historical_pronunciation_validated:false,production_whole_word_ready:false,analysis};
}
