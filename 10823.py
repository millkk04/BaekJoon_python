s=''
while True:
    try:
        line=input()
        s+=line
    except EOFError:
        break
x=list(map(int,s.split(',')))
print(sum(x))