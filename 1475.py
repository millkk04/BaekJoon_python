x=input()
k=[0]*9
for i in range(len(x)):
    y=int(x[i])
    if y==6:
        k[6]+=1
    elif y==9:
        k[6]+=1
    else:
        k[y]+=1
if k[6]%2!=0:
    k[6]+=1
k[6]=int(k[6]/2)

k.sort()

print(k[8])


