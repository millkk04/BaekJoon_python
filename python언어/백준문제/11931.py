import sys

input = sys.stdin.readline
output = sys.stdout.write

# 입력받을 숫자의 개수
N = int(input())

# 숫자를 저장할 리스트
y = []

# 숫자 입력 받기
for _ in range(N):
    q = int(input())
    y.append(q)

# 리스트를 오름차순으로 정렬
y.sort()

# 정렬된 리스트를 내림차순으로 출력
for i in range(N):
    output(f"{y[N-1-i]}\n")
