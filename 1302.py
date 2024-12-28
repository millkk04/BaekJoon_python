x=int(input())
y=dict()
for i in range(x):
    q=input()
    if q not in y:
        y[q]=1
    else:
        y[q]+=1
max_value = max(y.values())
max_key=[key for key,value in y.items() if value == max_value]
max_key.sort()
print(max_key[0])
