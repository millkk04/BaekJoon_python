x=input().upper()
y={}
for i in list(x):
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
max_value=max(y.values())
max_key=[key for key,value in y.items() if value == max_value]
if len(max_key)>=2:
    print("?")
else:
    print(max_key[0])





