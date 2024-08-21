N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

B.sort(reverse=True)
print(sum([a*b for a, b in zip(A, B)]))

