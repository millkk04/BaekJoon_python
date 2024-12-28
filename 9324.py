from collections import Counter
x=int(input())
final=[]
for _ in range(x):
    q=input()
    final.append(q)
for c in final:
    depend=True
    counter=Counter()

    for i in range(len(c)):
        counter[c[i]]+=1

        if i>=3:
            if counter[c[i-1]]>=3 and (counter[c[i-1]]-3)%4==0:
                if c[i-1]!=c[i]:
                    depend=False
                    break
    if depend:
        
        if counter[c[i]]>=3 and (counter[c[i]]-3)%4==0:
            if (i+1)==len(c):
                depend=False
            elif c[i]!=c[i+1]:
                depend=False

    if depend:
        print("OK")
    else:
        print("FAKE")


        


        

