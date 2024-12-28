n,L=map(int,input().split())
trying=list(map(int,input().split()))
trying.sort()
for i in range(n):
    if trying[i]<=L:
        L+=1
print(L)