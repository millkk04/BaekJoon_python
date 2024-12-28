t=int(input())
final=[]
for i in range(t):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a[1]=a[1]*2
    a[2]=a[2]*3
    a[3]=a[3]*3
    a[4]=a[4]*4
    a[5]=a[5]*10
    b[1]=b[1]*2
    b[2]=b[2]*2
    b[3]=b[3]*2
    b[4]=b[4]*3
    b[5]=b[5]*5
    b[6]=b[6]*10
    asum=0
    bsum=0
    for p in range(len(a)):
        asum+=a[p]
    for q in range(len(b)):
        bsum+=b[q]
    if asum>bsum:
        final.append("Good triumphs over Evil")
    elif asum < bsum:
        final.append("Evil eradicates all trace of Good")
    else:
        final.append("No victor on this battle field")
for k in range(len(final)):
    print(f"Battle {k+1}: {final[k]}")

    
    