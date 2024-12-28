t=int(input())
output=[list(map(int,input().split())) for _ in range(t)]
for i in range(t):
    a=int(str(output[i][0]),2)
    b=int(str(output[i][1]),2)
    x=a+b
    x=bin(x)
    print(x[2:])