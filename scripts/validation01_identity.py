"""Conservative physical-object identity for VALIDATION-01.
Only documented aliases are merged; uncertain identities require manual review.
"""
import re
import unicodedata

ALIASES = {
    'ORLEYL_V': ('ORLEYL V', 'ORLEYL-V', 'ORLEY V', 'F.9.5', 'F 9 5'),
    'ORLEYL_VII': ('ORLEYL VII', 'ORLEYL-VII', 'ORLEY VII', 'F.9.7', 'F 9 7'),
}
def normalize(value):
    s=unicodedata.normalize('NFKD', str(value or ''))
    s=''.join(c for c in s if not unicodedata.combining(c)).upper()
    return re.sub(r'[^A-Z0-9]+','',s)

INDEX={normalize(alias):key for key,aliases in ALIASES.items() for alias in aliases}
def identity(value):
    n=normalize(value)
    return INDEX.get(n, 'LITERAL:'+n) if n else ''
def identities(row):
    return {identity(row.get(k,'')) for k in ('object_id','physical_group') if identity(row.get(k,''))}
def declared_conflict(row):
    known={i for i in identities(row) if not i.startswith('LITERAL:')}
    return len(known)>1
