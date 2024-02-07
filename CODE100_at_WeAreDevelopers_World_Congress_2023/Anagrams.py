def anag(ch1,ch2):
    if len(ch1) != len(ch2):
        return False
    ch1 = sorted(ch1.lower())
    ch2 = sorted(ch2.lower())
    return (ch1 == ch2)

t = list(set([ "kiwi", "melon", "apple", "lemon" ]))
r = [] 
for i in range(len(t)-1):
    for j in range(i+1,len(t)):
        if anag(t[i],t[j]):
            r.append(t[i])
            r.append(t[j])
print(sorted(set(r)))