x=int(input())
y=[]
for _ in range(x):
    q=input()
    y.append(q)
k=y.copy()
k.sort() # 증가
a=k.copy()
k.sort(reverse=True)
b=k.copy() # 감소

if y==a:
    print('INCREASING')
elif y==b:
    print('DECREASING')
else:
    print('NEITHER')

