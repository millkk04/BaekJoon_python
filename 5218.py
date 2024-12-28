x=int(input())
output=[]
for i in range(x):
    a,b=input().split()
    y=[]
    for k in range(len(a)):
        if ord(b[k]) >= ord(a[k]):
            y.append(ord(b[k])-ord(a[k]))
        else:
            y.append(ord(b[k])+26-ord(a[k]))
    output.append(y)

for p in range(x):
    print("Distances: ",end='')
    for q in output[p]:
        print(q,end=' ')
    print()
    
