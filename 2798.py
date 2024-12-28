import itertools
x,y=map(int,input().split())

n=list(map(int,input().split()))

comb_n=list(itertools.combinations(n,3))

z=[]

for i in range(len(comb_n)):
    c=comb_n[i][0]+comb_n[i][1]+comb_n[i][2]
    z.append(c)
e=0
for k in z:
    if k<=y and k>e:
        e=k
print(e)
    
    
