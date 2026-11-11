# L35 Experimental metrology-family router

The L34 external test found no detections of the separately published
`ko/ti` editorial notation group in 35 Vieille-Toulouse tituli picti.
The new optional API separates the existing L32 `a/o/ki` family from
candidate `ko/ti` notation. It preserves spans, notation marks and abstention.

```python
from iberos.metrology_family_router_l35 import route
route("ko sss ti IIII")
route("a III")
```

**Research safeguards:**
- The `ko` and `ti` signs have *proposed* contextual/metrological
  interpretations in the literature, but this detector does not translate them.
- No numeric value, units converted, archaeological context or function is inferred.
- HGA.01.01–35 are now development records, not independent L35 validation.
- The local L35 development run finds 27 candidate records among 35, compared
  to 29/35 positive by the distinct L34 descriptive heuristic. This is **not
  27/29 semantic accuracy**; labels are not independently image verified.
- The fragment `ko s | ti` deliberately abstains.
- The module is opt-in, with no change to official Core metrics, default
  translation behavior or public web output.

**Tests:** `python -m unittest tests.test_metrology_family_router_l35 -v`.

Next: freeze this code and obtain image-checked complete-document negative
and positive controls from independent sites for prospective evaluation.
