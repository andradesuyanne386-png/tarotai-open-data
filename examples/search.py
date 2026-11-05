import json,sys
from pathlib import Path
cards=json.loads((Path(__file__).resolve().parents[1]/'data/cards.json').read_text())
query=' '.join(sys.argv[1:]).lower() or 'beginnings'
for c in cards:
    if query in ' '.join([c['name'],c['upright'],c['reversed']]).lower():
        print(c['name']+': '+c['upright']+'\n'+c['source_url'])
