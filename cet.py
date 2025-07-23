'''s={1,2,3,4,5}
ss={1,2,3}
sss={1,2,3,4,5,6}
print(s&ss&sss)'''

'''l=[1,2,3,2,4,5,1]
s=set()
for i in l:
    if l.count(i)>1 and i not in s:
        s.add(i)
print(s)'''
'''
n="education"
count=0
for i in n:
    if i in "AEIOUaeiou":
        count+=1
print(count)'''
'''
l=[[1,2,3],[3,4,5],[5,6]]
s=set()
for i in l:
    for j in i:
        s.add(j)
print(s)'''

'''a="hello"
b="world"
for i in a:
    if i in b:
        print("True")
        break
else:
    print("False")'''

'''a={1,2,3}
b={4,5,6}
k=7
aa=[]
for i in a:
    for j in b:
        if i+j==k:
            aa.append((i,j))
print(aa)'''

'''a={'a','b','c','d'}
word="bad"
op=True
for i in word:
    if i not in a:
        op=False
print(op)'''

'''a="apple"
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''

'''a={'a':1,'b':2}
aa={}
for k,v in a.items():
    aa[v]=k
print(aa)'''

'''a={1,2,3}
b={2,3,4}
c={3,4,5}
x=set()
for i in a:
    if i in b:
        x.add(i)
for i in b:
    if i in c:
        x.add(i)
print(len(x))'''

'''s="this is a test this is only a test"
a=s.split()
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''

a={'a':1,'b':2}
b={'b':3,'c':4}
x=a.keys()
xx=b.keys()
print(list(set(x)&set(xx)))








