import math

ft=input()
fs=input()

t=len(ft)
s=len(fs)

c=math.lcm(t,s)

t=c//t
s=c//s

if ft*t==fs*s:
    print(1)
else:
    print(0)