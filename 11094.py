x=int(input())
y=[]
for i in range(x):
    q=input()
    if q[0:10]=='Simon says':
        y.append(q[10:])
for i in range(len(y)):
    print(y[i])

        

