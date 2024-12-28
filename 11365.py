while True:
    x=input()
    if x=='END':
        break
    else:
        k=''
        for i in range(len(x)):
            k+=x[len(x)-1-i]
        print(k)