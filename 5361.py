x=int(input())

for i in range(x):
    total=0
    a,b,c,d,e=map(int,input().split())
    total+=a*350.34+b*230.90+c*190.55+d*125.30+e*180.90
    total="{:.2f}".format(total)
    print(f"${total}")