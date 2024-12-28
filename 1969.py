from collections import Counter
a,b=map(int,input().split())
final=[]

for i in range(a):
    q=input()
    final.append(q)

f=''

for i in range(b):
    k=''
    killing=0
    finish=[]
    for c in range(a):
        k+=final[c][i]
    
    counter=Counter(k)
    most_common_chars=counter.most_common()

    passing=most_common_chars[0][0]
    if len(most_common_chars)==1:
        f+=passing
    else:
        for checking in range(len(most_common_chars)):
            if counter[passing] == most_common_chars[checking][1]:
                killing+=1
            else:
                break
        for y in range(killing):
            finish.append(most_common_chars[y][0])
        f+=sorted(finish)[0]
cnt=0
for p in range(b):
    for q in range(a):
        if f[p]!=final[q][p]:
            cnt+=1
print(f)
print(cnt)
    
    

