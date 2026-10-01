from __future__ import annotations

import argparse
import json
from . import __version__
from .core import load_registry, get_object, family_objects, validate_result

def main():
    parser = argparse.ArgumentParser(prog="iberos", description="IberOS Open Research Kit CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("version")
    sub.add_parser("list-objects")

    p_show = sub.add_parser("show-object")
    p_show.add_argument("object_id")

    p_fam = sub.add_parser("family")
    p_fam.add_argument("family")

    p_val = sub.add_parser("validate")
    p_val.add_argument("json_file")

    args = parser.parse_args()

    if args.command == "version":
        print(f"IberOS Open Research Kit {__version__}")
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

if __name__ == "__main__":
    main()
