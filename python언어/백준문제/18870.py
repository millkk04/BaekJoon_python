import sys
from bisect import bisect_left

input=sys.stdin.readline
output=sys.stdout.write


x=int(input())

y=list(map(int,input().split()))

y_2=sorted(set(y))


less_count={}
for index,value in enumerate(y_2):
    less_count[value]=index

z=[]
for value in y:
    z.append(less_count[value])

for p in z:
    output(str(p)+' ')
        
    
