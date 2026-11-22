"""SCI-SEM-04: exact group-stratified observational permutation test for Bastida I.

Source-proposed gram equivalents are NOT measured gold; this tests association
of editorial suffix classes with quantities, not lexical roles or translation.
No dependencies beyond Python stdlib; no changes to core.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import argparse
import json
from pathlib import Path
from statistics import median

DATA = Path(__file__).resolve().parents[2] / "data/review/sci_sem04_bastida_19_entries_ferrer2026.json"


def _ranks(values: list[float]) -> list[float]:
    indexes = sorted(range(len(values)), key=lambda i: values[i])
    out = [0.0] * len(values)
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and values[indexes[end]] == values[indexes[start]]:
            end += 1
        avg_rank = (start + 1 + end) / 2
        for j in range(start, end):
            out[indexes[j]] = avg_rank
        start = end
    return out


def analyse(source: dict) -> dict:
    if source.get("schema") != "IberOS-SCI-SEM-04-Bastida19-Edition-Sourced/1.0":
        raise ValueError("Wrong schema")
    rows = source["entries"]
    if len(rows) != 19 or [r["sequence"] for r in rows] != list(range(1,20)):
        raise ValueError("Expected exactly 19 source-order entries")
    if [r["suffix_editorial"] for r in rows].count("ku") != 5:
        raise ValueError("Expected five documented ku entries")
    if [r["sequence"] for r in rows if r["suffix_editorial"] == "ku"] != [5,10,13,14,19]:
        raise ValueError("Original ku positions changed")
    groups = [[r for r in rows if r["operational_group"] == i] for i in range(1,5)]
    if [len(g) for g in groups] != [5,5,4,5]:
        raise ValueError("Wrong groups")
    if [sum(r["suffix_editorial"] == "ku" for r in g) for g in groups] != [1,1,2,1]:
        raise ValueError("Wrong group-label structure")
    for r in rows:
        if r["image_read_independently"] is not False or r["measurement_status"] != "HYPOTHETICAL_CONVERTED_GRAMS_NOT_DIRECT_PHYSICAL_WEIGHT":
            raise ValueError("Unjustified primary reading or metrological gold")
        if type(r["grams_editorial_ferrer2026"]) not in (float,int) or r["grams_editorial_ferrer2026"] <= 0:
            raise ValueError("Invalid weight estimate")
    ka = [r["grams_editorial_ferrer2026"] for r in rows if r["suffix_editorial"] == "ka"]
    ku = [r["grams_editorial_ferrer2026"] for r in rows if r["suffix_editorial"] == "ku"]
    rank_groups = [_ranks([r["grams_editorial_ferrer2026"] for r in g]) for g in groups]
    observed = sum(rank_groups[i][j] for i,g in enumerate(groups) for j,r in enumerate(g) if r["suffix_editorial"]=="ku")
    alternatives = [list(combinations(range(len(g)),sum(r["suffix_editorial"]=="ku" for r in g))) for g in groups]
    reference = [sum(rank_groups[i][j] for i,chosen in enumerate(choices) for j in chosen) for choices in product(*alternatives)]
    n_ge = sum(stat >= observed-1e-10 for stat in reference)
    return {
        "schema":"IberOS-SCI-SEM-04-Exact-Stratified-Permutation/1.0",
        "rows":len(rows),"physical_artifacts":1,
        "ka_entries":len(ka),"ku_entries":len(ku),
        "median_ka_editorial_g":median(ka),"median_ku_editorial_g":median(ku),
        "mean_ka_editorial_g":round(sum(ka)/len(ka),5),
        "mean_ku_editorial_g":round(sum(ku)/len(ku),5),
        "operational_group_sizes":[len(g) for g in groups],
        "ku_count_per_group":[sum(r["suffix_editorial"]=="ku" for r in g) for g in groups],
        "observed_stratified_ku_rank_sum":observed,
        "exact_assignments":len(reference),
        "one_sided_assignments_ge_observed":n_ge,
        "conditional_one_sided_p":n_ge/len(reference),
        "null_hypothesis":"Within each of the four published operational groups, ka/ku labels are exchangeable, with the observed number of ku labels fixed.",
        "warning":"Selection, autocorrelation, preexisting editorial direction hypothesis, corrected numbers, and model-based grams prohibit causal or lexical inference; not prospective or independent replication.",
        "exception":"beŕśir: a ka record at sequence 18 estimated to 549.5 g",
        "semantic_gold":False,"semantic_success_count":0,
        "actual_translation_demonstrated":False,
        "core_modified":False,"cost_eur":0,
    }


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--input",type=Path,default=DATA)
    p.add_argument("--output",type=Path)
    args=p.parse_args(argv)
    result=json.dumps(analyse(json.loads(args.input.read_text(encoding="utf-8"))),ensure_ascii=False,indent=2)+"\n"
    if args.output:
        if args.output.resolve()==args.input.resolve():
            raise ValueError("Cannot overwrite raw source")
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(result,encoding="utf-8")
    else: print(result,end="")


if __name__=="__main__":
    main()
