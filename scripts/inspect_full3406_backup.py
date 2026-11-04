"""Backwards-compatible CLI wrapper for IberOS FULL3406 ZIP inspector."""
from iberos.full3406_backup import main


if __name__ == "__main__":
    raise SystemExit(main())
