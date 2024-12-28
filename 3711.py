N=int(input())
finish=[]
for _ in range(N):
    output=[]
    test=[]
    depend=[]
    cnt=1
    G=int(input())
    for i in range(G):
        q=int(input())
        output.append(q)
    test=output.copy()
    if len(output)==1:
        finish.append(1)
    else:
        while True:
            for k in range(len(output)):
                test[k]=output[k]%cnt
            depend=test.copy()
            
            depend=list(set(depend))
            if len(depend)==len(output):
                finish.append(cnt)
                break
            else:
                cnt+=1

for p in range(len(finish)):
    print(finish[p])




