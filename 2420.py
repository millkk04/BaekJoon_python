a,b=input().split()
a=int(a)
b=int(b)
sum = a-b
if sum<0:
    sum=b-a
print(sum)