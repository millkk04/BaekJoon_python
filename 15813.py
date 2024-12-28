x=int(input())
cnt=0
q=input()
for i in range(x):
    cnt+=ord(q[i])-64
print(cnt)
