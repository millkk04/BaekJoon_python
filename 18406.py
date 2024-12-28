n=input()
y=len(n)
x=len(n)//2
n=list(n)
p=0
q=0
for a in range(x):
    p+=int(n[a])
for b in range(x,y):
    q+=int(n[b])
if p==q:
    print("LUCKY")
else:
    print("READY")