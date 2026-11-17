# IberOS-Read · visual baseline 01 (experimental)

This is an isolated prototype. It **does not change the validated Core**, metrics, C594/C474/C539/C541, or Write.

## What already exists in IberOS-Write

`site/write/index.html` maps 26 conventional north-eastern Iberian sign values to named Wikimedia SVG glyphs: a/e/i/o/u, l/m/n/r/ŕ/s, ba/be/bi/bo/bu, ta/te/ti/to/tu, ka/ke/ki/ko/ku. These are *selected graphic variants*, not a full palaeographic inventory. Segmentation also mentions ś/z/ḿ without equivalent graphic entries in this mapping. The Write fallback maps **modern Spanish to approximate Iberian-style glyphs**; its source recovery is not ancient decipherment.

## What this baseline can do

Given a local archaeological image, a JSON list of **human-defined sign crops**, and local reference PNGs labelled by conventional sign value, `reader.py` reports the best image-similarity candidates, abstains below threshold or on ambiguous results, and records hashes of image, boxes and reference files. No editorial transcription is used by the classifier. Never equate these scores to calibrated probabilities.

Install zero-cost local dependencies:

```bash
python -m pip install numpy opencv-python
python research/iberos_read/reader.py --image sample.png --boxes boxes.json --templates reference_png/ --output result.json
python -m unittest discover -s research/iberos_read -p 'test_*.py'
```

`boxes.json` example: `[{"x": 100, "y": 40, "w": 32, "h": 55}]`.

Template filenames: `a__reference01.png`, `ka__reference02.png`, `ŕ__reference03.png`. Reference PNGs must contain **a single sign** with a contrasting background. Use locally licensed reference glyphs or crop known signs under permitted usage; no resources or images are automatically downloaded. For scientific testing, **template and test objects must be physically independent** and be split by PHYS_ID/LEAK_GROUP.

## What it cannot do yet

- Automatically locate and split touching signs or lines.
- Reliably read worn, rotated, partial, scribal or variant glyphs.
- Infer an unknown sign or provide meaning/translation.
- Establish recognition accuracy on independently held-out real photographs.
- Use generated Write glyph images as independent archaeological verification.

## Acceptance gate

1. Obtain openly usable real photographs and independently audited palaeographic reference glyphs.
2. Lock physical object IDs and a TRAIN / HOLD split with no source leakage.
3. Pre-register thresholds, uncertainty/abstention and error measures.
4. Freeze predictions before revealing editorial ground truth; report sign error rate, per-class confusion, coverage, abstentions and corrupt crops.
5. Require independent human adjudication before any Core promotion.

**State:** infrastructure implementation, experimental, NOT VALIDATED. The first tests are synthetic smoke tests, not real recognition benchmarks.
