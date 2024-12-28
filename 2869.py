# a,b,v=map(int,input().split())
# k=0
# day=1
# while True:
#     k+=a
#     if k>=v:
#         print(day)
#         break
#     k-=b
#     day+=1
a,b,v=map(int,input().split())
day=(v-b-1)//(a-b)+1
print(day)