
stc=input()
check=False
for a in range(len(stc)):
    if 'U'==stc[a]:
        for b in range(a,len(stc)):
            if 'C'==stc[b]:
                for c in range(b,len(stc)):
                    if 'P'==stc[c]:
                        for d in range(c,len(stc)):
                            if 'C'==stc[d]:
                                check=True
                                break
                        break
                break
        break

if check:
    print("I love UCPC")
else:
    print("I hate UCPC")