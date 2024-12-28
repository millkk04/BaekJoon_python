output=[]
for i in range(9):
    q=int(input())
    output.append(q)
d=output.copy()
d.sort()

y=d[8]

for j in range(9):
    if output[j]==y:
        break
print(y)
print(j+1)