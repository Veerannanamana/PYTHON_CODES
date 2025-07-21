def CountOddEven(n,l):
    Even=0
    Odd=0
    for i in l:
        if i%2==0:
            Even+=1
        else:
            Odd+=1
    print(Odd-Even)
n=int(input())
l=list(map(int,input().split()))
CountOddEven(n,l)


def findcatencount(n,l):
    count=0
    for i in l:
        count+=(i//12)
    return count
n=int(input())
l=list(map(int,input().split()))
print(findcatencount(n,l))

n=int(input())
x=bin(n)[2:]
y=""
for i in x:
    if i==str(1):
        y+=str(0)
    else:
        y+=str(1)
print(int(y,8))
