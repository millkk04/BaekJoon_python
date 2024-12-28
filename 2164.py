from collections import deque

x=int(input())
y=deque()

for k in range(1,x+1):
    y.append(k)

for i in range(x-1):
    y.popleft()
    y.rotate(-1)
print(y[0])

    


