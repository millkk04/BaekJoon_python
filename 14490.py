import math
n,m=input().split(":")
n,m=int(n),int(m)
c=math.gcd(n,m)
n=n//c
m=m//c
print(f"{n}:{m}")
