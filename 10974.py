from itertools import permutations

x=int(input())
y=[]
for i in range(x):
    y.append(i+1)
output=list(permutations(y,x))

# for k in range(len(output)):
#     for p in range(x):
#         print(output[k][p],end=' ')
#     print()
for k in range(len(output)):
    print(" ".join(map(str,output[k])))