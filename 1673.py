while True:
    try:
        n,k=map(int,input().split())
        x=n
        y=0
        while n>=k:
            x+=n//k
            n=(n//k)+(n%k)
        print(x)
    except:
        break
