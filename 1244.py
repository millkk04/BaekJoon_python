x=int(input())
xlist=list(map(int,input().split()))
cnt=int(input())

for i in range(cnt):
    a,b=map(int,input().split())

    if a==1:
        for p in range(x):
            if (p+1)%b==0:
                if xlist[p]==0:
                    xlist[p]=1
                else:
                    xlist[p]=0
    else:
        if b==1 or b==x:
            if xlist[b-1]==0:
                xlist[b-1]=1
            else:
                xlist[b-1]=0
        else:
            if (b/x)>=0.5:
                for q in range(x-b+1):
                    if xlist[b-1-q]==xlist[b-1+q]:
                        if xlist[b-1-q]==0:
                            xlist[b-1-q],xlist[b-1+q]=1,1
                        else:
                            xlist[b-1-q],xlist[b-1+q]=0,0
                    else:
                        break
            else:
                for q in range(b):
                    if xlist[b-1-q]==xlist[b-1+q]:
                        if xlist[b-1-q]==0:
                            xlist[b-1-q],xlist[b-1+q]=1,1
                        else:
                            xlist[b-1-q],xlist[b-1+q]=0,0
                    else:
                        break

for k in range(len(xlist)):
    print(xlist[k],end=' ')
    if (k+1)%20==0:
        print()