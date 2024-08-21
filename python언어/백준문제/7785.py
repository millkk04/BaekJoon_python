import sys

input=sys.stdin.readline
output=sys.stdout.write

x=int(input())
y=[]
for i in range(x):
    q1,q2=input().split()
    if i==0:
        dic={q1:q2}
    else:
        dic[q1]=q2
for r in dic:
    if dic[r]=='enter':
        y.append(r)
y.sort(reverse=True)
for k in y:
    output(k+'\n')

        
    

    
        
        
    
