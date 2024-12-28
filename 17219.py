import sys

input = sys.stdin.readline
output = sys.stdout.write

x,y=map(int,input().split())

xl,yl=[],[]
z=[]
order=[]

for i in range(x):
    q1,q2=input().split()
    xl.append(q1)
    z.append(q2)
    
for j in range(y):
    qy=input().strip()
    yl.append(qy)

index_map = {name: i for i, name in enumerate(xl)}

for k in yl:
    order.append(index_map[k])

for p in order:
    output(z[p]+'\n')
    
        
    
