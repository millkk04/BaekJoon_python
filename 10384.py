n=int(input())
eng=[]
y=[]
op=[]
for i in range(n):
    q1=input()
    eng.append(q1)

for i in eng:
    for x in range(len(i)):
        if i[x].isalpha():
            