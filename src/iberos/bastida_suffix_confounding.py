"""SCI-SEM-05: sensitivity and person-identity confounding audit for SCI-SEM-04.

This module does not infer meanings. With no individual observed with both
suffixes, the suffix effect is not identifiable independently of person.
"""
from __future__ import annotations
from itertools import combinations, product
from collections import defaultdict
from pathlib import Path
import json
from .bastida_exact_morpheme_test import DATA


def exact_stratified(rows: list[dict]) -> dict:
    """One-sided exact rank permutation, group-conditional, variable subset size."""
    groups = [[r for r in rows if r["operational_group"] == g] for g in range(1, 5)]
    candidates = []
    observed = 0.0
    for group in groups:
        masses = [r["grams_editorial_ferrer2026"] for r in group]
        ranks = [
            sum(z < v for z in masses) + (sum(z == v for z in masses) + 1) / 2
            for v in masses
        ]
        k = sum(r["suffix_editorial"] == "ku" for r in group)
        observed += sum(rank for rank, row in zip(ranks, group) if row["suffix_editorial"] == "ku")
        candidates.append([
            sum(ranks[i] for i in ids)
            for ids in combinations(range(len(group)), k)
        ])
    if not all(candidates):
        raise ValueError("Empty stratum")
    all_values = [sum(values) for values in product(*candidates)]
    n_ge = sum(value >= observed - 1e-10 for value in all_values)
    return {
        "rows": len(rows), "observed_ku_rank_sum": observed,
        "assignments": len(all_values), "as_or_more_extreme": n_ge,
        "p_one_sided_conditional": n_ge / len(all_values)
    }


def analyse(source: dict) -> dict:
    rows = source["entries"]
    if len(rows) != 19 or source.get("physical_objects") != 1:
        raise ValueError("Expected the complete single-artifact editorial series")
    by_name = defaultdict(list)
    for row in rows:
        by_name[row["person_editorial"]].append(row)
    crossed_names = sorted(name for name, rr in by_name.items()
                           if len(set(r["suffix_editorial"] for r in rr)) > 1)
    ku_names = sorted(name for name, rr in by_name.items()
                      if any(r["suffix_editorial"] == "ku" for r in rr))
    if len(ku_names) != 2 or ku_names != ["aiduaŕgi", "saldulako"] or crossed_names:
        raise ValueError("Unexpected source grouping; inspect editions")
    controls = {
        "all_19": rows,
        "without_beŕśir_high_549_5": [r for r in rows if r["sequence"] != 18],
        "without_all_beŕśir": [r for r in rows if r["person_editorial"] != "beŕśir"],
        "without_editorially_corrected": [r for r in rows if r["editorial_uncertainty"] != "CORRECTION_ANNOTATED"],
    }
    return {
        "schema": "IberOS-SCI-SEM-05-Sensitivity-Confounding/1.0",
        "distinct_names":len(by_name),
        "ku_names": ku_names,
        "ku_name_count":len(ku_names),
        "names_with_both_suffixes":crossed_names,
        "suffix_separable_from_person_within_artifact":False,
        "person_conditioned_label_swaps_possible":0,
        "sensitivity":{key:exact_stratified(value) for key,value in controls.items()},
        "warning":"Within-person effect cannot be estimated: all repeated persons are suffix-invariant. Group-stratified p values measure quantity-suffix association under exchangeable labels, not identity-adjusted evidence for a lexical translation; leave-outs are retrospective.",
        "editorial_conversion_is_external_gold":False,
        "semantic_direction_confirmed":False,
        "blind_semantic_success_count":0,
        "core_modified":False,"cost_eur":0,
    }


if __name__ == "__main__":
    print(json.dumps(analyse(json.loads(DATA.read_text(encoding="utf-8"))),
                     indent=2,ensure_ascii=False))
