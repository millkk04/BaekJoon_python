x=input()
y=int(input())
cnt=0
for _ in range(y):
    z=input()
    z=z+z

    if x in z:
        cnt+=1
print(cnt)
