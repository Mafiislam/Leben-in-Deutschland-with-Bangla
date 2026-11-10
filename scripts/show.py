"""Print a compact batch of source questions for translation: python3 -I scripts/show.py <from> <to> | states:<slug>"""
import json, sys
b = json.load(open('data/base.json', encoding='utf-8'))
a = sys.argv[1]
if a.startswith('s:'):
    qs = [q for q in b['questions'] if q['state'] == a[2:]]
else:
    lo, hi = int(a), int(sys.argv[2]); qs = [q for q in b['questions'] if not q['state'] and lo <= q['n'] <= hi]
for q in qs:
    img = all(o['de'].startswith('Bild ') for o in q['opts'])
    print(f"[{q['id']}] {q['en']}" + ('  <IMAGE OPTIONS: translate q and x only>' if img else ''))
    if not img:
        for i, o in enumerate(q['opts']): print(f"  {i}{'*' if i == q['correct'] else ' '} {o['en']}")
    print(f"  x: {q['exp_en']}")
