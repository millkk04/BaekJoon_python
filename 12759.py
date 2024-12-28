ttt=[['1','2','3'],['4','5','6'],['7','8','9']]
x=int(input())
cnt=0
output=[]
for k in range(9):
    y=list(map(int,input().split()))
    output.append(y)



for i in range(9):
    cnt+=1
    if cnt%2!=0:
        ttt[output[i][1]-1][output[i][0]-1]='O'
        player=x
    else:
        ttt[output[i][1]-1][output[i][0]-1]='X'
        player=2 if x==1 else 1
    # print(ttt[0])
    # print(ttt[1])
    # print(ttt[2])
    # print('\n')

    if (ttt[0][0]==ttt[0][1]==ttt[0][2] or
        ttt[1][0]==ttt[1][1]==ttt[1][2] or
        ttt[2][0]==ttt[2][1]==ttt[2][2] or
        ttt[0][0]==ttt[1][0]==ttt[2][0] or
        ttt[0][1]==ttt[1][1]==ttt[2][1] or
        ttt[0][2]==ttt[1][2]==ttt[2][2] or
        ttt[0][0]==ttt[1][1]==ttt[2][2] or
        ttt[0][2]==ttt[1][1]==ttt[2][0]):
        print(player)
        break
#print(cnt)
else:
    print(0)
