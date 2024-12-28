n=int(input())
x=list(input())
a,b=0,0
for i in range(n):
    if x[i]=='A':
        a+=1
    else:
        b+=1
if a>b:
    print('A')
elif b>a:
    print('B')
else:
    print("Tie")