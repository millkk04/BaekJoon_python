output=[]
while True:
    x=input()
    cnt=0
    if x=='#':
        break
    else:
        for i in range(len(x)):
            if x[i] in ['a','e','i','o','u','A','E','I','O','U']:
                cnt+=1
        output.append(cnt)
for q in range(len(output)):
    print(output[q])