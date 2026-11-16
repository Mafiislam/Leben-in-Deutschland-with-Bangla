"""Merges data/base.json with translations/bn/*.json into data/questions.json.
Translation file format: {"<question id>": {"q": "...", "o": ["a","b","c","d"], "x": "explanation"}}
and optional {"_states": {"<slug>": "Bangla state name"}}."""
import json, glob, re, sys
base = json.load(open('data/base.json', encoding='utf-8'))
tr, st = {}, {}
for f in sorted(glob.glob('translations/bn/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    st.update(d.pop('_states', {}))
    tr.update(d)
missing = []
for s in base['states']:
    s['name_bn'] = st.get(s['slug'], '')
    if not s['name_bn']: missing.append('state:' + s['slug'])
for q in base['questions']:
    t = tr.get(q['id'])
    # De/En fields stay as they are; Bangla fields are added next to them.
    if re.fullmatch(r'Bild \d', q['opts'][0]['de'] or ''):
        for i, o in enumerate(q['opts']): o['bn'] = 'ছবি ' + '০১২৩৪৫৬৭৮৯'[i + 1]
    if not t:
        missing.append(q['id']); continue
    q['bn'] = t['q']
    if 'o' in t:
        for o, v in zip(q['opts'], t['o']): o['bn'] = v
    q['exp_bn'] = t.get('x', '')
    q['opts'] = q['opts']
# Per-option notes (why each answer is right or wrong): translations/oe/<lang>/*.json = {"<id>": ["note A", "B", "C", "D"]}
for lang in ('en', 'de', 'bn'):
    oe = {}
    for f in sorted(glob.glob(f'translations/oe/{lang}/*.json')):
        oe.update(json.load(open(f, encoding='utf-8')))
    for q in base['questions']:
        if q['id'] in oe: q['oe_' + lang] = oe[q['id']]
    print('option notes', lang, len(oe))
json.dump(base, open('data/questions.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('merged', len(tr), 'translations; questions still without Bangla:', len(missing))
if '--strict' in sys.argv and missing: print(missing[:20]); sys.exit(1)
