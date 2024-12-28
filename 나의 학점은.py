x= list(map(int, input().split()))
a=input()
t=0
k=0
while t<50:
    if int(a)>=int(x[t]):
        k+=1
        t+=1
    else:
        t+=1
if k>=46:
    print('A+')
elif 36<=k<=45:
    print('A0')
elif 21<=k<=35:
    print('B+')
elif 16<=k<=20:
    print('B0')
elif 6<=k<=15:
    print('C+')
elif 3<=k<=5:
    print('C0')
else:
    print('F')
    
