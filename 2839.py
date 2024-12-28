x=int(input())
n=0
depend=1
while x>=3:
    if x%5==0:
        n+=(x//5)
        x=0
        print(n)
        depend=0
        break
    else:
        n+=1
        x-=3
if x==1 or x==2:
    print(-1)
if depend==1 and x==0:
    print(n)
