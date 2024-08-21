x=input()
y=input()
a=0
b=0

for i in range(int(x)):
    if y[i]=='2':
        a+=1
    elif y[i]=='e':
        b+=1
if a>b:
    print(2)
elif a<b:
    print('e')
elif a==b:
    print('yee')
    
        

    
    



    
