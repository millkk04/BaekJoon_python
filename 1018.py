n,m=map(int,input().split())
final=[]
output=[input() for _ in range(n)]
for p in range(n-8+1):
    for q in range(m-8+1):
        cnt1=0
        cnt2=0
        if output[p][q]=='B':
            x='B'
            for a in range(8):
                for b in range(8):
                    if output[a+p][b+q]!=x:
                        cnt1+=1
                    if output[a+p][b+q]==x:
                        cnt2+=1
                    if b!=7 and x=='B':
                        x='W'
                    elif b!=7 and x=='W':
                        x='B'
        else:
            x='W'
            for a in range(8):
                for b in range(8):
                    if output[a+p][b+q]!=x:
                        cnt1+=1
                    if output[a+p][b+q]==x:
                        cnt2+=1
                    if b!=7 and x=='B':
                        x='W'
                    elif b!=7 and x=='W':
                        x='B'
        final.append(min(cnt1,cnt2))
final.sort()
print(final[0])