x=input()
a=[]
for i in range(4):
    a.append(x[i])

if a[0]=='E':
    a[0]='I'
else:
    a[0]='E'

if a[1]=='N':
    a[1]='S'
else:
    a[1]='N'

if a[2]=='T':
    a[2]='F'
else:
    a[2]='T'

if a[3]=='P':
    a[3]='J'
else:
    a[3]='P'

output=''
for i in range(4):
    output+=a[i]
print(output)
