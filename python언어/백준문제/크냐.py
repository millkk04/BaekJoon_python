i=0

while True:
    a=list(range(0,i))
    b=list(range(0,i))
    a[i],b[i]=input().split()
    i+=1
    if a == 0 and b == 0:
        break
i=0
while a[i]==0 and b[i]==0:
    if int(a[i]) > int(b[i]):
        print('Yes')
        i+=1
    else:
        print('No')
        i+=1
    
