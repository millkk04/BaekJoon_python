n,m=map(int,input().split())
output=[list(map(int,input().split())) for _ in range(n)]
output.sort(key=lambda x: [x[1],x[2],x[3]],reverse=True)
for i in range(n):
    if m==output[i][0]:
        break
for j in range(n):
    if output[i][1:]==output[j][1:]:
        print(j+1)
        break
