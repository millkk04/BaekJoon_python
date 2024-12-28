def check(x):
    global cnt
    if len(str(x))==n:
        if x%3==0:
            cnt+=1
        return
    for i in range(3):
        check(10*x+i)


n=int(input())
cnt=0
check(1)
check(2)
print(cnt)