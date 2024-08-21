x=input()
y=[]
for i in range(len(x)):
    y.append(x[i])
y.sort(reverse=True)
prt=''
for p in y:
    prt=prt+p
print(prt)
