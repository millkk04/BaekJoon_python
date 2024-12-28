cnt=0
while True:
    cnt+=1
    death=0
    o,w=map(int,input().split())
    if o==0 and w==0:
        break
    else:
        while True:
            a,b=input().split()
            b=int(b)
            if a=='#' and b==0:
                break
            else:
                if a=='F':
                    w+=b
                elif a=='E':
                    w-=b
                if w<=0:
                    death=1
        print(cnt,end=" ")
        if death==1:
            print("RIP")
        else:
            if w > o/2 and w < o*2:
                print(":-)")
            else:
                print(":-(")

                