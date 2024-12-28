n,m=map(int,input().split())
output=[list(map(int,input().split())) for _ in range(2)]
final=output[0]+output[1]
final.sort()

for i in final:
    print(i,end=' ')