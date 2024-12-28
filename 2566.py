outlist=[list(map(int,input().split())) for _ in range(9)]
check=outlist[0][0]
a,b=0,0
for p in range(9):
    for q in range(9):
        if check<outlist[p][q]:
            check=outlist[p][q]
            a,b=p,q
print(check)
print(a+1,b+1)        