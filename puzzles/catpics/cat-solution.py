import json 

with open('catdata.json','r') as f :
  data = json.load(f)
names = set()
maxw = 0
maxh = 0
form= {}
for i in data:
  name = i["alt"][:i["alt"].find(":")]
  names.add(name)
  maxw = max(maxw,i["width"])
  maxh = max(maxh,i["height"])
  if i["filename"][i["filename"].find('.')+1:] not in form:
    form[i["filename"][i["filename"].find('.')+1:]] = 1
  else:
    form[i["filename"][i["filename"].find('.')+1:]] +=1
res = {"uniquenames": len(names),"widest" : maxw,"tallest":maxh,"formats":form}
print(res)