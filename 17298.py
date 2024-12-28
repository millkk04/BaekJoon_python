# from collections import deque

# N = int(input())

# A = deque(list(map(int,input().split())))

# B = A.copy()

# output = []
# for i in range(N-1):
#     d = False
#     ex = any(num > B[i] for num in A)

#     if ex:

#         for p in range(len(A)):

#             if A[p] > B[i]:
#                 output.append(A[p])
#                 d = True
#                 break
#     if d:
#         pass
#     else:
#         output.append(-1)
        
#     A.popleft()

# output.append(-1)

# for q in output:
#     print(q,end=' ')

# from collections import deque
# N = int(input())
# A = deque(list(map(int,input().split())))

# B=[]

# output=[]

# for i in range(N-1):
#     d = False
#     for k in range(i+1,N):
#         if A[i] < A[k]:
#             output.append(A[k])
#             d = True
#             break
#     if d:
#         pass
#     else:
#         output.append(-1)
# output.append(-1)
# for p in output:
#     print(p,end=' ')

# from collections import deque
# N = int(input())
# A = deque(list(map(int,input().split())))

# B=A.copy()
# B.popleft() # 계속 변화하는 값
# C=B.copy() # 고정 값
# output=[]
# for i in range(N-1):
#     c = len(B)
#     for k in range(c):
#         if A[i] < B[0]:
#             output.append(B[0])
#             break
#         else:
#             B.popleft()
#     if len(B)==0:
#         B=C.copy()
#         output.append(-1)
# output.append(-1)
# for p in output:
#     print(p,end=' ')

N=int(input())
A=list(map(int,input().split()))
stack=[]
output=[-1]*N

for i in range(N-1,-1,-1):

    while len(stack)!=0 and stack[-1] <= A[i]:
        stack.pop()
    
    if len(stack)!=0:
        output[i]=stack[-1]
    
    stack.append(A[i])

for p in output:
    print(p,end=' ')

    



    
    
        


        






