with open('puzzle.json', 'r') as f:
    string = f.read()

#using iteration throught characters
s = 0
f = 0
for c in string :
    if c.isdigit():
        s = s * 10 + int(c)
    else :
        f += s
        s = 0
f += s
print ("Resut :\n",f)
#using iteration throught index 

s = 0
f = 0
for i in range(len(string)):
    if string[i].isdigit():
        s = s *10 + int(string[i])
    else:
        f+=s
        s=0
f+=s
print("Resut :\n", f)
#using regex
import re 
numbers =[int(C) for C in re.findall(r'\d+', string)]
f  = sum(numbers)
print ("Resut :\n",f)