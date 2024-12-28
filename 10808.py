x=input()
xlist=[0]*26

for i in x:
    xlist[ord(i)-97]+=1

for j in xlist:
    print(j,end=' ')