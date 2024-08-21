
######

while True:
    try:
        s,t=input().split()
        cnt=0
        k=0
        for i in range(len(t)):
            if cnt==len(s):
                break
            else:
                if t[i]==s[k]:
                    cnt+=1
                    k+=1
        if cnt==len(s):
            print('Yes')
        else:
            print('No')
    except:
        break
        




