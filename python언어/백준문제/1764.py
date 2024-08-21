import sys
input = sys.stdin.readline
output = sys.stdout.write


N, M = map(int, input().strip().split())


lis = []
sil = []


for _ in range(N):
    lis.append(input())


for _ in range(M):
    sil.append(input())


s = sorted(set(lis) & set(sil))
s.sort()

print(len(s))
for k in s:
    output(k)

            

    
