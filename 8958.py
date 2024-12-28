x=int(input())
cnt=1
score=0
output=[]
for i in range(x):
    q=input()
    cnt=1
    score=0
    for j in range(len(q)):
        if q[j]=='O':
            score+=cnt
            cnt+=1
        elif q[j]=='X':
            cnt=1
    output.append(score)
for n in range(x):
    print(output[n])


