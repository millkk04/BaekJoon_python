x=input()
cnt=0
for word in list(x):
    if ord(word)>=97:
        cnt+=ord(word)-96
    else:
        cnt+=ord(word)-38
d=0
for i in range(2,cnt):
    if cnt%i==0:
        print("It is not a prime word.")
        d=1
        break
if d==0:
    print("It is a prime word.")

