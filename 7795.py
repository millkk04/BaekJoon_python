import bisect

t=int(input())
N=[]
A=[]
B=[]
for _ in range(t):
    N.append(list(map(int,input().split())))
    A.append(list(map(int,input().split())))
    B.append(list(map(int,input().split())))
for i in range(t):
    cnt=0
    B[i].sort()
    for p in A[i]:
        cnt+=bisect.bisect_left(B[i],p)
    print(cnt)