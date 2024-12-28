y={}
while True:
    try:
        q=list(input().split())
        for i in q:
            for p in list(i):
                if p not in y:
                    y[p]=0
                else:
                    y[p]+=1
    except:
        max_value=max(y.values())
        max_key=[key for key,value in y.items() if value == max_value]
        max_key.sort()
        for k in range(len(max_key)):
            print(max_key[k],end='')
        break


