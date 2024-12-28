x=list(map(int,input().split()))
a=x[0]
sum=0
for k in range(len(x)):
    sum+=x[k]
    if a>x[k]:
        a=x[k]
cnt=0

for p in range(len(x)):
    if a==x[p]:
        break
    else:
        cnt+=1
if sum>=100:
    print('OK')
else:
    if cnt==0:
        print("Soongsil")
    elif cnt==1:
        print("Korea")
    elif cnt==2:
        print("Hanyang")