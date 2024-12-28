n=int(input())
output=[list(map(int,input().split())) for _ in range(n)]
output.sort(key=lambda x: [-x[0],x[1]])
checking=output[4][0]
cnt=0
for i in range(5,n):
    if output[i][0]==checking:
        cnt+=1
    else:
        break
print(cnt)