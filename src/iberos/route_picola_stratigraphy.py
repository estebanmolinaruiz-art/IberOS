"""G-126: independent chronology and provenance audit for La Picola NE gate.
Preserved, restored and hypothesized features must never be conflated.
"""
from dataclasses import dataclass, asdict

VALID={"excavated","restored","hypothesis","unverified"}

@dataclass(frozen=True)
class Feature:
    key: str
    classification: str
    source: str
    observation: str
    start: int | None = None
    end: int | None = None
    stratigraphy_verified: bool = False
    crossing_feature: bool = False
    panel: str = ""

    def __post_init__(self):
        if self.classification not in VALID or not self.key or not self.source:
            raise ValueError("Invalid feature or missing provenance")
        if self.start is not None and self.end is not None and self.start>self.end:
            raise ValueError("Inverted chronology")

def evaluate(features: list[Feature], period=(-429,-349)) -> dict:
    lo,hi=period
    if lo>hi: raise ValueError("Invalid period")
    qualifies=[]
    excluded=[]
    for f in features:
        direct=(f.classification=="excavated" and f.crossing_feature
                and f.stratigraphy_verified and f.start is not None
                and f.end is not None and f.start<=lo<=hi<=f.end)
        entry={**asdict(f),"qualified_direct_crossing":direct}
        (qualifies if direct else excluded).append(entry)
    return {
        "case":"PICOLA-NE-G126","period":[lo,hi],
        "figure3_dark":"preserved","figure3_light":"restored",
        "crossing_review_candidates":qualifies,"unqualified":excluded,
        "bridge_or_causeway_confirmed":False,
        "historical_road_confirmed":False,
        "verdict":"REQUIRES_EXTERNAL_REVIEW" if qualifies else "NO_DIRECT_DATED_CROSSING_EVIDENCE",
        "note":"Even dated excavated remains are candidates for independent review, not proof by software."
    }

def picola_1998_case():
    s="Moret and Badie 1998, AEspA 71, pp. 54-56, figs. 2-3"
    return evaluate([
        Feature("northeast_curtain","excavated",s,"NE curtain conserved; not a bridge",panel="fig3"),
        Feature("street_R2","excavated",s,"R2 excavated in 1995; axis leads to NE gate",panel="fig3"),
        Feature("northeast_gate","excavated",s,"Located near center of NE curtain, but no dated exterior crossing",panel="fig3"),
        Feature("moat_sections","excavated",s,"Ditch documented, no specific crossing identified",panel="fig3"),
        Feature("defence_profile","restored",s,"Figure 2 is an explicitly reconstructed profile",panel="fig2"),
        Feature("lost_segments","restored",s,"Figure 3 light grey is restored geometry",panel="fig3"),
        Feature("bridge_hypothesis","hypothesis",s,"No independently dated crossing structure in this article",crossing_feature=True,panel="interpretation")
    ])
