n=int(input())

a=list(map(int,input().split()))

m=int(input())

b=list(map(int,input().split()))

a=set(a)

for t in b:
    if t in a:
        print(1)
    else:
        print(0)
    
    
