x=int(input())
outlist=[list(map(int,input().split())) for _ in range(x)]
check=[[outlist[a][0] for a in range(x)],[outlist[b][1] for b in range(x)],[outlist[c][2] for c in range(x)]]
final=[0 for _ in range(x)]
for p in range(x):
    for q in range(3):
        cnt=0
        for i in range(x):
            if outlist[p][q]==check[q][i]:
                cnt+=1
        if cnt<2:
            final[p]+=outlist[p][q]
for k in range(x):
    print(final[k])
            