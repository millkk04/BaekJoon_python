x=input() # 문자 입력
n=len(x) # 문자 수
x=list(x) # x를 리스트로 변경

for i in range(1, int(n ** 0.5) + 1): # n의 제곱근까지 실행
    if n%i==0:
        r=i     # r = 행 , c = 열
        c=int(n/i)
output=[[] for _ in range(r)] # r값만큼 행 만들기
cnt=0
for p in range(c): 
    for q in range(r): # 각 행 별로 문자 넣어주기
        output[q].append(x[cnt]) 
        cnt+=1
        
for k in range(r):           # 해독된 메시지 출력
    for j in range(c):
        print(output[k][j],end='')