"""Independent computational controls; no interpretation or Core mutation."""
from collections import Counter

def leave_one_group_out(records, group_key="leak_group", value_key="sequence"):
    """Report held-out groups and overlapping sequences without fitting a model."""
    groups = {}
    for record in records:
        group = record[group_key]
        groups.setdefault(group,[]).append(record[value_key])
    result = {}
    for group, sequences in groups.items():
        other = {s for g, vals in groups.items() if g != group for s in vals}
        result[group] = {"n":len(sequences),"overlap_with_other_groups":sum(s in other for s in sequences)}
    return result

def terminal_counts(records, sequence_key="signs", group_key="leak_group"):
    """Counts terminal signs after deduplicating exact sequence within leak group."""
    seen=set(); counts=Counter()
    for record in records:
        signs=tuple(record[sequence_key]); key=(record[group_key],signs)
        if signs and key not in seen:
            seen.add(key); counts[signs[-1]]+=1
    return dict(counts)

def image_pair_manifest(pairs):
    """Prepare photo/drawing comparison manifest; no unverified glyph classification."""
    out=[]
    for p in pairs:
        for key in ("phys_id","photo_sha256","drawing_sha256","source","license"):
            if not p.get(key): raise ValueError("Missing "+key)
        out.append({**p,"classification":"INDETERMINATE","human_review_required":True})
    return out
