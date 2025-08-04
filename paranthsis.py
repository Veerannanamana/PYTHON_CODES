n=input()
mapping={']':'[','}':'{',')':'('}
s=[]
isvalid=True
for i in n:
    if i in "{([":
        s.append(i)
    elif i in ")}]":
        if not s or s[-1]!=mapping[i]:
            isvalid=False
            break
        else:
            s.pop()
if isvalid:
    print(True)
else:
    print(False)
