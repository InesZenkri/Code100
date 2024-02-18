import json

with open('puzzle.json', 'r') as f:
    data = json.load(f)

tt = {}
res = []
for t in data:
    if t['ship'] in tt:
        res[tt[t['ship']]]['crewcount'] += 1
    else:
        tt[t['ship']] = len(res)
        res.append({'ship': t['ship'], 'crewcount': 1})
print(res)