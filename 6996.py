n=int(input())

for i in range(n):
    a,b = input().split()
    A = sorted(list(a))
    B = sorted(list(b))
    if A==B:
        print("{} & {} are anagrams.".format(a,b))
    else:
        print("{} & {} are NOT anagrams.".format(a,b))



