from collections import Counter
n=int(input())
f=[]
for i in range(n+1):
    q=list(input().split())
    for k in range(len(q)):
        f.append(q[k])
final=Counter(f)
final=final.most_common()
for j in range(len(final)):
    print(f"{final[j][0]} {final[j][1]-1}")

