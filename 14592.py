n=int(input())
output=[list(map(int,input().split())) for _ in range(n)]
final=output.copy()
output.sort(key=lambda x: [-x[0],x[1],x[2]])
for i in range(n):
    if output[0]==final[i]:
        break
print(i+1)
