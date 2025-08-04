rows=int(input())
cols=int(input())
a=[]
for i in range(rows):
    a.append(list(map(int,input().split())))
l=[]
for i in range(rows+cols-1):
    t=[]
    for j in range(len(a)):
        for k in range(len(a[j])):
            if j+k==i:
                t.append(a[j][k])
    l.append(t)
for i in range(len(l)):
    if i%2==0:
        print(*l[i][::-1],end=" ")
    else:
        print(*l[i],end=" ")
