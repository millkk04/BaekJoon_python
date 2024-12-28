# n=int(input())

# final=[]
# number=['0','1','2','3','4','5','6','7','8','9']
# finish=[]

# for _ in range(n):
#     q=input()
#     final.append(q)

# for stc in final:
#     ex=''
#     cnt=0
#     i=0
#     while cnt < len(stc):
#         if stc[cnt] in number:
#             ex+=stc[cnt]
#             while True:
#                 i+=1
#                 if (cnt+i)<=len(stc)-1 and stc[cnt+i] in number:
#                     continue
#                 else:
#                     break
#             for r in range(i):
#                 if i!=1 and (cnt+r+1) <= len(stc)-1:
#                     ex+=stc[cnt+r+1]
#                 else:
#                     break
#             finish.append(ex)
#             cnt+=(1+i)
#             i=0
#             ex=''
#             break
#         else:
#             cnt+=1
#     if stc[len(stc)-1] in number:
#         finish.append(stc[len(stc)-1])
# print(finish)

n=int(input())

final=[]
number=['0','1','2','3','4','5','6','7','8','9']
finish=[]

for _ in range(n):
    q=input()
    final.append(q)

for stc in final:
    ex=''
    for i in range(len(stc)):
        if stc[i] in number:
            








    