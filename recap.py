stack=[]
s="datastruct"

for ch in s:
    stack.append(ch)

reversedstring=" "

while stack:
    reversedstring += stack.pop()

print(reversedstring)