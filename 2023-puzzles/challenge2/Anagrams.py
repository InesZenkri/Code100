import json
with open('./puzzle.json', 'r') as f:
  t = json.load(f)
  f.close() 
tt = {}
for i in t:
  key = ''.join(sorted(i))
  if key in tt:
    tt[key].append(i)
  else:
    tt[key] = [i]

values = [val for value in tt.values() for val in value if len(value) > 1]
print(sorted(values))