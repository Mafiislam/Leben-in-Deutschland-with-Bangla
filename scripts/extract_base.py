"""Builds data/base.json (German + English only) from the upstream quiz-data.json.
Upstream: https://github.com/abdullahbutt/leben-in-deutschland-test
(German questions: BAMF catalogue; English text and explanations: upstream, CC BY-NC 4.0)."""
import json, sys
src = sys.argv[1]
d = json.load(open(src, encoding='utf-8'))
qs = []
for q in d['general']:
    qs.append(dict(id=str(q['id']), n=q['id'], state=None, image=q.get('image'), correct=q['correct'],
                   de=q['de'], en=q['en'], opts=[dict(de=o['de'], en=o['en']) for o in q['options']],
                   exp_de=q.get('exp_de', ''), exp_en=q.get('exp_en', '')))
states = []
for slug, v in d['states'].items():
    states.append(dict(slug=slug, name_de=v['name_de'], name_en=v['name_en']))
    for i, q in enumerate(v['questions']):
        qs.append(dict(id=q['id'], n=301 + i, state=slug, image=q.get('image'), correct=q['correct'],
                       de=q['de'], en=q['en'], opts=[dict(de=o['de'], en=o['en']) for o in q['options']],
                       exp_de=q.get('exp_de', ''), exp_en=q.get('exp_en', '')))
json.dump(dict(version=d.get('version'), states=states, questions=qs), open('data/base.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(qs), 'questions,', len(states), 'states')
