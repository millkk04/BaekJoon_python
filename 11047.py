x,y=map(int,input().split())
price=[]
for i in range(x):
    p=int(input())
    price.append(p)
c=0
for k in reversed(range(len(price))):
    c+=y//price[k]
    y%=price[k]
print(c)
        
    
