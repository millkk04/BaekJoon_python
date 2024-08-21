x,y=map(int,input().split())

p=[]

for i in range(x):
    p.append(i+1)

from itertools import permutations

q=list(permutations(p,y))

for i in  range(len(q)):
    for k in range(y):
        print(q[i][k],end=' ')
    print()

    
    

