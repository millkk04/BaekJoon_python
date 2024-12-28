for i in range(3):
    x=input()
    max_len=0
    cnt=1
    for p in range(1,len(x)):
        if x[p-1]==x[p]:
            cnt+=1
        else:
            cnt=1

        if cnt>max_len:
            max_len=cnt
    print(max_len)