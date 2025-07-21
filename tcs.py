def position(n,l,k):
    a=l[k-1:]
    b=[]
    for i in range(len(a)-1):
        b.append(abs(a[i]-a[i+1]))
    return sum(b)
n=int(input())
l=list(map(int,input().split()))
k=int(input())
print(position(n,l,k))
