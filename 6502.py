i=1
while True:
    x=list(map(int,input().split()))
    if x[0]==0:
        break
    r,w,l=x
    dp=(w/2)**2+(l/2)**2
    if r**2 >= dp:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")
    i+=1