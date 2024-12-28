a=int(input())
output=[]
for i in range(a):
    k=''
    x,y=input().split()
    x=int(x)
    for j in range(len(y)):
        k+=y[j]*x
    output.append(k)
for p in range(len(output)):
    print(output[p])
    