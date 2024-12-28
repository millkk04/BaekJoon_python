n=int(input())
output=[]
for i in range(n):
    name,a,b,c=input().split()
    output.append([name,int(a),int(b),int(c)])

output.sort(key=lambda x:[-x[1],x[2],-x[3],x[0]])

for k in range(n):
    print(output[k][0])