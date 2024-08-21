t=int(input())
i=0
A=list(range(t))
B=list(range(t))
while i<t:
    A[i],B[i]=input().split()
    i+=1
k=0
n=1
while k<i:
    print("Case #"+str(n)+":",A[k],'+',B[k],'=',int(A[k])+int(B[k]))
    k+=1
    n+=1
     
    
