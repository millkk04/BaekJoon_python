x=input()
cnt=0
for i in range(len(x)):
    if x[i]==' ':
        cnt+=1
cnt+=1
if x[0]==' ':
    cnt-=1
if x[len(x)-1]==' ':
    cnt-=1
print(cnt)