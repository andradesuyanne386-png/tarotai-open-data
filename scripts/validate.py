import csv,json
from pathlib import Path
from collections import Counter
r=Path(__file__).resolve().parents[1]
c=json.loads((r/'data/cards.json').read_text())
assert len(c)==78 and len({x['card_id'] for x in c})==78
assert Counter(x['arcana'] for x in c)=={'major':22,'minor':56}
assert sorted(Counter(x['suit'] for x in c if x['arcana']=='minor').values())==[14]*4
for x in c:
    for key in ['name','upright','reversed','keywords_upright','keywords_reversed','source_url']:
        assert x[key], (x['card_id'],key)
    assert x['locale']=='en' and x['source_url'].startswith('https://tarotai.art/')
assert [json.loads(x) for x in (r/'data/cards.jsonl').read_text().splitlines()]==c
with (r/'data/cards.csv').open() as f:
    rows=list(csv.DictReader(f))
assert len(rows)==78
for original,row in zip(c,rows):
    for key,value in original.items():
        expected=json.dumps(value) if isinstance(value,list) else '' if value is None else str(value)
        assert row[key]==expected
s=json.loads((r/'data/spreads.json').read_text())
assert len(s)==10 and len({x['spread_id'] for x in s})==10
for x in s:
    assert x['reflection_question'] and x['positions']
    assert [p['index'] for p in x['positions']]==list(range(1,len(x['positions'])+1))
print('PASS: 78 unique cards, 22/56 split, four suits, required fields, matching exports, 10 spreads')
