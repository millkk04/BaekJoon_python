x=int(input())
for p in range(x):
    k=[i for i in range(65,91)]
    for u in input():
        k[ord(u)-65]=0
    print(sum(k))
