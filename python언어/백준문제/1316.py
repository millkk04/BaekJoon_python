x=int(input())
y=0
for i in range(x):
    q=input()
    z=[]
    for k in range(len(q)):
        if q[k] in z:
            if q[k] != q[k-1]:
                y+=1
                break
        else:
            z.append(q[k])
print(x-y)
        
