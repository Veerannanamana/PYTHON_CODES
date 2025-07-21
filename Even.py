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
