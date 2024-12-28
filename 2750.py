x=int(input())
output=[]
for i in range(x):
    q=int(input())
    output.append(q)
output.sort()
for q in range(len(output)):
    print(output[q])
