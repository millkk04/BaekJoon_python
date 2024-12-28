x=input()
k=''
for i in range(len(x)):
    k+=x[i]
    if len(k)==10:
        print(k)
        k=''
print(k)

