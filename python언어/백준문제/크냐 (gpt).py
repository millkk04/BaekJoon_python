i = 0
a = []
b = []

# 사용자가 '0 0'을 입력할 때까지 입력을 받습니다.
while True:
    input_str = input()
    x, y = input_str.split()
    if x == '0' and y == '0':
        break
    a.append(int(x))
    b.append(int(y))
    i += 1

# 리스트 a와 b의 각 원소를 비교합니다.
for j in range(i):
    if a[j] > b[j]:
        print('Yes')
    else:
        print('No')
