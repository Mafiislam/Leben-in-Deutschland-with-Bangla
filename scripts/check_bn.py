"""Validates translation files: valid JSON, right number of options, no stray ASCII double quotes issues."""
import json, glob, sys
b = json.load(open('data/base.json', encoding='utf-8'))
by = {q['id']: q for q in b['questions']}
bad = 0; n = 0
for f in sorted(glob.glob('translations/bn/*.json')):
    try: d = json.load(open(f, encoding='utf-8'))
    except Exception as e: print('INVALID JSON', f, e); bad += 1; continue
    d.pop('_states', None)
    for k, v in d.items():
        n += 1
        q = by.get(k)
        if not q: print('unknown id', k, f); bad += 1; continue
        img = all(o['de'].startswith('Bild ') for o in q['opts'])
        if not v.get('q') or not v.get('x'): print('empty q/x', k); bad += 1
        if not img and len(v.get('o', [])) != 4: print('options!=4', k); bad += 1
        if any(not x.strip() for x in v.get('o', [])): print('empty option', k); bad += 1
print(n, 'entries checked,', bad, 'problems'); sys.exit(1 if bad else 0)
