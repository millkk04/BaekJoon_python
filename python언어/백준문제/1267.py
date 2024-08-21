x=int(input())
y=list(map(int,input().split()))

a=0
b=0

for i in range(x):


        a+=(y[i]//30)+1

a=a*10

for i in range(x):

        b+=(y[i]//60)+1

b=b*15

if a>b:
    print('M',b)
elif a<b:
    print('Y',a)
elif a==b:
    print('Y','M',a)
