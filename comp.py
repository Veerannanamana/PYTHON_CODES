'''
l=["python","java","c"]
ll=[i.upper() for i in l ]
print(ll)
'''
'''
s='comprehension'
result={i for i in s if i in "AEIOUaeiou"}
print(result)
'''
'''l=["python","java","c"]
ll={i:len(i) for i in l }
print(ll)'''
'''s='java'
result={i:s.count(i) for i in s}
print(result)'''
'''a=[1,4,6,9,11]
re=[(a[i],a[j]) for i in range(len(a)-1) for j in range(i,len(a)) if (a[i]+a[j])%5==0]
print(re)'''
'''a=[[1,2],[3,4],[5,6]]
re=[j**2 for i in a for j in i if j%2==1]
print(re)'''
l=["python"," java"]
ll=''.join(["*" if j in "aeiou" else j for i in l for j in i])
print(ll)









