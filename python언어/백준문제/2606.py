computer = int(input())

network = int(input())

v=[1]

count=[]

for i in range(network):
    p,q=map(int,input().split())

    count.append([p,q])
count.sort()
for _ in range(100):
    for k in range(network):
        
        if count[k][0] in v or count[k][1] in v:
            v.append(count[k][0])
            v.append(count[k][1])

v=set(v)

print(len(v)-1)
    
    
