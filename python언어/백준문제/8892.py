from itertools import permutations

t=int(input())
y=[] # 출력 값
for _ in range(t):
    k=int(input())
    x=[] # 선별
    z=[] # 문장 최종 선별


    for _ in range(k):
        stc=input()
        x.append(stc)


    words = list(permutations(x,2))
    
    success=0
    for pair in words:
        cbw=pair[0]+pair[1]
        d=True

        for i in range(int(len(cbw)//2)):
            if cbw[i] != cbw[len(cbw)-1-i]:
                d=False
                break
        if d:
            y.append(cbw)
            success=1
            break

    if success!=1:
        y.append(0)
for p in y:
    print(p)

        

            




