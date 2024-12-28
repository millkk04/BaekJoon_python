T=int(input())
output=[]
for _ in range(T):
    c=list(map(int,input().split()))
    output.append(c)
for i in range(T):
    if output[i][0:2]==output[i][3:5]:
        if output[i][2]==output[i][5]:
            print(-1)
        else:
            print(0)
    else:
        L=output[i][2]+output[i][5]
        d=((output[i][0]-output[i][3])**2+(output[i][1]-output[i][4])**2)**(1/2)

        if L > d:
            if output[i][2]==d+output[i][5] or output[i][5]==d+output[i][2]:
                print(1)
            elif output[i][2]>d+output[i][5] or output[i][5]>d+output[i][2]:
                print(0)
            else:
                print(2)
        elif L == d:
            print(1)
        else:
            print(0)  