x,y=map(int,input().split())
cnt=[0 for j in range(x)]
outlist=[list(map(int,input().split())) for _ in range(y)]

for i in range(y):
    cnt[outlist[i][0]-1]+=1
    cnt[outlist[i][1]-1]+=1
    if [outlist[i][1],outlist[i][0]] in outlist[i:y]:
        cnt[outlist[i][0]-1]-=1
        cnt[outlist[i][1]-1]-=1

for k in range(x):
    print(cnt[k])