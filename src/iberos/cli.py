from __future__ import annotations

import argparse
import json

from . import __version__
from .core import (
    engine_status,
    evaluate_bi_context,
    family_objects,
    get_object,
    load_registry,
    rhotic_search_key,
    rok_semantic_guard,
    validate_result,
    validate_rhotic_usage,
    registry_independence_audit,
    family_gate_policy,
    family_dashboard,
    family_bottlenecks,
)


def main():
    parser = argparse.ArgumentParser(prog="iberos", description="IberOS Open Research Kit CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("version")
    sub.add_parser("status")
    sub.add_parser("list-objects")

    p_show = sub.add_parser("show-object")
    p_show.add_argument("object_id")

    p_fam = sub.add_parser("family")
    p_fam.add_argument("family")

    p_val = sub.add_parser("validate")
    p_val.add_argument("json_file")

    p_bi = sub.add_parser("guard-bi")
    p_bi.add_argument("--quantitative", action="store_true")
    p_bi.add_argument("--verbal-complex", action="store_true")

    p_rhotic = sub.add_parser("rhotic-search-key")
    p_rhotic.add_argument("signature")

    p_rguard = sub.add_parser("guard-rhotic")
    p_rguard.add_argument("purpose")
    p_rguard.add_argument("--neutralized", action="store_true")

    sub.add_parser("audit-independence")

    sub.add_parser("dashboard")
    sub.add_parser("bottlenecks")

    p_policy = sub.add_parser("family-policy")
    p_policy.add_argument("family")

    p_rok = sub.add_parser("guard-rok")
    p_rok.add_argument("--literal")

    args = parser.parse_args()

    if args.command == "version":
        print(f"IberOS Open Research Kit {__version__}")
    elif args.command == "status":
        print(json.dumps(engine_status(), ensure_ascii=False, indent=2))
    elif args.command == "list-objects":
        for row in load_registry():
            print(f'{row["OBJECT_ID"]}\t{row["Nombre_objeto"]}\t{row["IberOS_Inclusion"]}')
    elif args.command == "show-object":
        row = get_object(args.object_id)
        if not row:
            raise SystemExit(f"Object not found: {args.object_id}")
        print(json.dumps(row, ensure_ascii=False, indent=2))
    elif args.command == "family":
        rows = family_objects(args.family)
        for row in rows:
            print(f'{row["OBJECT_ID"]}\t{row["Nombre_objeto"]}')
    elif args.command == "validate":
        ok, errors = validate_result(args.json_file)
        if ok:
            print("VALID")
        else:
            print("INVALID")
            for e in errors:
                print(f"- {e}")
            raise SystemExit(2)
    elif args.command == "guard-bi":
        print(json.dumps(evaluate_bi_context(
            independently_quantitative=args.quantitative,
            verbal_complex=args.verbal_complex,
        ), ensure_ascii=False, indent=2))
    elif args.command == "rhotic-search-key":
        print(rhotic_search_key(args.signature))
    elif args.command == "guard-rhotic":
        print(json.dumps(validate_rhotic_usage(
            purpose=args.purpose,
            neutralized=args.neutralized,
        ), ensure_ascii=False, indent=2))
    elif args.command == "dashboard":
        print(json.dumps(family_dashboard(), ensure_ascii=False, indent=2))
    elif args.command == "bottlenecks":
        print(json.dumps(family_bottlenecks(), ensure_ascii=False, indent=2))
    elif args.command == "family-policy":
        print(json.dumps(family_gate_policy(args.family), ensure_ascii=False, indent=2))
    elif args.command == "audit-independence":
        print(json.dumps(registry_independence_audit(), ensure_ascii=False, indent=2))
    elif args.command == "guard-rok":
        print(json.dumps(rok_semantic_guard(args.literal), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
