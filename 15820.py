n,m=map(int,input().split())
check=0
sample=[list(map(int,input().split())) for _ in range(n)]
system=[list(map(int,input().split())) for _ in range(m)]
for p in range(n):
    if sample[p][0]!=sample[p][1]:
        print("Wrong Answer")
        check=1
        break
if check==0:
    for q in range(m):
        if system[q][0]!=system[q][1]:
            print("Why Wrong!!!")
            check=1
            break
if check==0:
    print("Accepted")