stc=[]
comp=[]
dic={}
q=''
while True:
    if q==0:
        break
    else:
        q=int(input())
        if q==0:
            break
        else:
            for i in range(q):

                x=input()
                y=x.lower()
                dic[y]=x
                comp.append(y)
                
            comp.sort()
            

            stc.append(dic[comp[0]])

            comp=[]
            dic={}
for k in range(len(stc)):
    print(stc[k])
            
