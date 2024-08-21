a,b=input().split()
if int(a)>int(b):
    a=a*int(a)
    for i in range(int(b)):
        print(a[i],end='')
else:
    b=b*int(b)
    for i in range(int(a)):
        print(b[i],end='')
