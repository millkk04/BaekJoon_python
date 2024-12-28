x=input()
x=list(x)
stack=[]
temp=1
cnt=0
for i in range(len(x)):
    if x[i]=='(':
        stack.append(x[i])
        temp*=2
    elif x[i]=='[':
        stack.append(x[i])
        temp*=3
    elif x[i]==')':
        if not stack or stack[-1] =='[':
            cnt=0
            break
        if x[i-1]=='(':
            cnt+=temp
        stack.pop()
        temp//=2

    else:
        if not stack or stack[-1]=='(':
            cnt=0
            break
        if x[i-1]=='[':
            cnt+=temp
        stack.pop()
        temp//=3
if stack:
    print(0)
else:
    print(cnt)