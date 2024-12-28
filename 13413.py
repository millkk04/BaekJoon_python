n=int(input()) #입력 수
final=[]    #테스트 데이터
passing=[]  #final에 넣을 케이스들

for _ in range(n): #final에 넣는 과정
    for i in range(3):
        q1=input()
        passing.append(q1)
    final.append(passing)
    passing=[]

for _ in range(n): #검사과정
    check_1=0   #2개의 말 서로의 위치를 바꾼다.
    check_2=0   #말 1개를 들어 뒤집어 놓아 변경한다.
    while True:
        if final[n][1]==final[n][2]:
            break
        else:
            for k in range(int(final[n][0])-1):
                if final[n][1][k]!=final[n][2][k]:
                    ex=final[n][1]


                           


