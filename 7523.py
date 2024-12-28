n=int(input())
digits=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    a,b=digits[i][0],digits[i][1]
    sum=(b-a+1)*(a+b)//2
    print(f"Scenario #{i+1}:")
    print(sum,'\n')