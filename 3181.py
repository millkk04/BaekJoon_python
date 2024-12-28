x=list(input().split())
y=''
y+=(chr(ord(x[0][0])-32))

for i in range(1,len(x)):
    if x[i] not in ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']:
        y+=(chr(ord(x[i][0])-32))
print(y)