n=input()
a=len(n)
b=len(n)//10
c=len(n)%10
for i in range(b):
    for x in range(i*10,(9+10*i)):
        if x%10==0 and x!=0:
            print('\'n[x],end='')
        else:
            print(n[x],end='')
        
            
    
