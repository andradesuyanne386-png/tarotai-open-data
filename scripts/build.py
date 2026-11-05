import csv, json
from pathlib import Path
r = Path(__file__).resolve().parents[1]
cards = json.loads((r/'data/cards.json').read_text())
(r/'data/cards.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in cards))
with (r/'data/cards.csv').open('w', newline='') as f:
    out = csv.DictWriter(f, fieldnames=list(cards[0]))
    out.writeheader()
    out.writerows({k:json.dumps(v) if isinstance(v,list) else v for k,v in c.items()} for c in cards)
