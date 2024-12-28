n,m=map(int,input().split())
t=int(input())
a,b=0,m-1
cnt=0
for i in range(t):
    x=int(input())
    x-=1
    if x<a:
        for k in range(n):
            if a-k<=x<=b-k:
                a=a-k
                b=b-k
                break
            else:
                cnt+=1
    elif x>b:
        for k in range(n):
            if a+k<=x<=b+k:
                a=a+k
                b=b+k
                break
            else:
                cnt+=1
    else:
        continue
print(cnt)

