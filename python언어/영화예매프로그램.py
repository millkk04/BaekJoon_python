#로그인 및 회원가입 부분
print('***주의) 답변은 "네", "아니요"로 대답해주세요.***') #프로그램의 오류 방지
print()
answer=input('안녕하세요, 회원이신가요? ') #회원인지 아닌지 체크하는 과정
ty=0 #로그인 시도 횟수 제한 변수
if answer=='아니요': # 기존 아이디가 없는 경우
    print()
    print('회원가입을 진행해주세요.')
    print()
    userid=input('아이디: ')
    password=input('비밀번호: ')
    print()
    print('회원가입이 완료되었습니다,')
    
    while True:
        print()
        answer_userid=input('아이디를 입력해주세요: ')
        answer_password=input('비밀번호를 입력해주세요: ')
        if answer_userid==userid and answer_password==password:
            break
        elif answer_userid==userid and answer_password!=password:
            print('비밀번호가 틀렸습니다.')
        elif answer_userid!=userid and answer_password==password:
            print('아이디가 틀렸습니다.')
        elif answer_userid!=userid and answer_password!=password:
            print('없는 회원정보입니다.')
        elif answer_userid!=userid and answer_password!=password:
            print('없는 회원정보입니다.')

else: #기존 아이디가 있는 경우
    userid=None
    password=None

    while ty<3: #실수로 아이디가 없는데 있다고 입력한 경우에 빠져나오는 시스템
        print()
        answer_userid=input('아이디를 입력해주세요: ')
        answer_password=input('비밀번호를 입력해주세요: ')
        if answer_userid==userid and answer_password==password:
            break
        elif answer_userid==userid and answer_password!=password:
            print('비밀번호가 틀렸습니다.')
        elif answer_userid!=userid and answer_password==password:
            print('아이디가 틀렸습니다.')
        elif answer_userid!=userid and answer_password!=password:
            print('없는 회원정보입니다.')
            ty+=1
        elif answer_userid!=userid and answer_password!=password:
            print('없는 회원정보입니다.')
            ty+=1

    answer_try=input('회원가입을 진행할까요?')
    if answer_try=='네':
        print()
        userid=input('아이디: ')
        password=input('비밀번호: ')
        print()
        print('회원가입이 완료되었습니다,')
    
        while True:
            print()
            answer_userid=input('아이디를 입력해주세요: ')
            answer_password=input('비밀번호를 입력해주세요: ')
            if answer_userid==userid and answer_password==password:
                break
            elif answer_userid==userid and answer_password!=password:
                print('비밀번호가 틀렸습니다.')
            elif answer_userid!=userid and answer_password==password:
                print('아이디가 틀렸습니다.')
            elif answer_userid!=userid and answer_password!=password:
                print('없는 회원정보입니다.')
            elif answer_userid!=userid and answer_password!=password:
                print('없는 회원정보입니다.')
    elif answer_try=='아니요':
            while True:
                print()
                answer_userid=input('아이디를 입력해주세요: ')
                answer_password=input('비밀번호를 입력해주세요: ')
                if answer_userid==userid and answer_password==password:
                    break
                elif answer_userid==userid and answer_password!=password:
                    print('비밀번호가 틀렸습니다.')
                elif answer_userid!=userid and answer_password==password:
                    print('아이디가 틀렸습니다.')
                elif answer_userid!=userid and answer_password!=password:
                    print('없는 회원정보입니다.')
                elif answer_userid!=userid and answer_password!=password:
                    print('없는 회원정보입니다.')




end=0 #영화 예매하려는 횟수 변수

seat=['A','B','C','D','E','F','G','H','I','J']

a_list=[]
for i in seat:
    for j in range(1,11,1):
        a_list.append(i+str(j))

b_list=[]
for i in seat:
    for j in range(1,11,1):
        b_list.append(i+str(j))

c_list=[]
for i in seat:
    for j in range(1,11,1):
        c_list.append(i+str(j))

d_list=[]
for i in seat:
    for j in range(1,11,1):
        d_list.append(i+str(j))

e_list=[]
for i in seat:
    for j in range(1,11,1):
        e_list.append(i+str(j))

print()
ra,rb,rc,rd,re=0,0,0,0,0

def a_seat():
    global ra,end
    
    if ra==0:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    print('□',end='')
                else:
                    if j==2 or j==8:
                        print('□',end='   ')
                    else:
                        print('□',end='')
            print()
        
    else:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    if (i+str(j)) in a_list:
                        print('□',end='')
                    else:
                        print('■',end='')
                else:
                    if j==2 or j==8:
                        if (i+str(j)) in a_list:
                            print('□',end='   ')
                        else:
                            print('■',end='   ')
                    else:
                        if (i+str(j)) in a_list:
                            print('□',end='')
                        else:
                            print('■',end='')
                            
            print()
    print('입니다.')
    print()
    pe_a=int(input('몇 좌석을 예매하실건가요? (ex. 2자리가 예약하고싶으면 2 라고 입력)>> '))
    print()
    while pe_a>0:
        pe_a-=1
        reser_a=input('어떤 좌석을 예약하실건가요? (하나씩 입력) ex. A1 >>')
        if reser_a in a_list:
            ra+=1
            for i in range(100):
                if a_list[i]==reser_a:
                    break
                else:
                    pass
            a_list[i]=a_list[i]+'1'
            
            for i in seat:
                for j in range(1,11,1):
                    if j==1:
                         print(i,end=' ')
                         if (i+str(j)) in a_list:
                             
                             print('□',end='')
                        
                         else:
                             
                             print('■',end='')
                    else:
                        if j==2 or j==8:
                            if (i+str(j)) in a_list:
                                print('□',end='   ')
                            else:
                                print('■',end='   ')
                        else:
                            if (i+str(j)) in a_list:
                                print('□',end='')
                            else:
                                print('■',end='')
                print()
            
        else:
            print('예매할 수 없는 좌석입니다.')
            pe_a+=1

    while True:
        aaa=input('혹시 예매를 취소할 좌석이 있나요?')
        if aaa=='네':
            aaaa=input('어느 좌석을 예매 취소할까요?')
            if aaaa not in a_list:
                for i in range(100):
                    if (a_list[i])[0]+(a_list[i])[1]==aaaa:
                        
                        break
                    else:
                        pass
                
                a_list[i]=aaaa

                for i in seat:
                    for j in range(1,11,1):
                        if j==1:
                             print(i,end=' ')
                             if (i+str(j)) in a_list:
                             
                                 print('□',end='')
                        
                             else:
                             
                                 print('■',end='')
                        else:
                            if j==2 or j==8:
                                if (i+str(j)) in a_list:
                                    print('□',end='   ')
                                else:
                                    print('■',end='   ')
                            else:
                                if (i+str(j)) in a_list:
                                    print('□',end='')
                                else:
                                    print('■',end='')
                    print()

                
                
                aa=input('예매를 취소할 좌석이 더 있나요?')
                if aa=='네':
                    continue
                elif aa=='아니요':
                    break
            else:
                print('예매되지 않은 좌석입니다.')
            
        elif aaa=='아니요':
            break
        

            
    reser_a1=input('추가로 예매할 좌석이 있으신가요? ')
    if reser_a1=='네':
        end=0
    elif reser_a1=='아니요':
        end=1
        print('프로그램을 종료하겠습니다.')

def b_seat():
    global rb,end
    if rb==0:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    print('□',end='')
                else:
                    if j==2 or j==8:
                        print('□',end='   ')
                    else:
                        print('□',end='')
            print()
        
    else:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    if (i+str(j)) in b_list:
                        print('□',end='')
                    else:
                        print('■',end='')
                else:
                    if j==2 or j==8:
                        if (i+str(j)) in b_list:
                            print('□',end='   ')
                        else:
                            print('■',end='   ')
                    else:
                        if (i+str(j)) in b_list:
                            print('□',end='')
                        else:
                            print('■',end='')
                            
            print()
    print('입니다.')
    print()
    pe_b=int(input('몇 좌석을 예매하실건가요? (ex. 2자리가 예약하고싶으면 2 라고 입력)>> '))
    print()
    while pe_b>0:
        pe_b-=1
        reser_b=input('어떤 좌석을 예약하실건가요? (하나씩 입력) ex. A1 >>')
        if reser_b in b_list:
            rb+=1
            for i in range(100):
                if b_list[i]==reser_b:
                    break
                else:
                    pass
            b_list[i]=b_list[i]+'1'
            for i in seat:
                for j in range(1,11,1):
                    if j==1:
                         print(i,end=' ')
                         if (i+str(j)) in b_list:
                             
                             print('□',end='')
                        
                         else:
                             
                             print('■',end='')
                    else:
                        if j==2 or j==8:
                            if (i+str(j)) in b_list:
                                print('□',end='   ')
                            else:
                                print('■',end='   ')
                        else:
                            if (i+str(j)) in b_list:
                                print('□',end='')
                            else:
                                print('■',end='')
                print()
            
        else:
            print('예매할 수 없는 좌석입니다.')
            pe_b+=1

    while True:
        bbb=input('혹시 예매를 취소할 좌석이 있나요?')
        if bbb=='네':
            bbbb=input('어느 좌석을 예매 취소할까요?')
            if bbbb not in b_list:
                for i in range(100):
                    if (b_list[i])[0]+(b_list[i])[1]==bbbb:
                        break
                    else:
                        pass
                b_list[i]=bbbb

                for i in seat:
                    for j in range(1,11,1):
                        if j==1:
                             print(i,end=' ')
                             if (i+str(j)) in b_list:
                             
                                 print('□',end='')
                        
                             else:
                             
                                 print('■',end='')
                        else:
                            if j==2 or j==8:
                                if (i+str(j)) in b_list:
                                    print('□',end='   ')
                                else:
                                    print('■',end='   ')
                            else:
                                if (i+str(j)) in b_list:
                                    print('□',end='')
                                else:
                                    print('■',end='')
                    print()


                
                bb=input('예매를 취소할 좌석이 더 있나요?')
                if bb=='네':
                    continue
                elif bb=='아니요':
                    break
            else:
                print('예매되지 않은 좌석입니다.')
            
        elif bbb=='아니요':
            break
        

            
    reser_b1=input('추가로 예매할 좌석이 있으신가요? ')
    if reser_b1=='네':
        end=0
    elif reser_b1=='아니요':
        end=1
        print('프로그램을 종료하겠습니다.')

    
def c_seat():
    global rc,end
    if rc==0:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    print('□',end='')
                else:
                    if j==2 or j==8:
                        print('□',end='   ')
                    else:
                        print('□',end='')
            print()
        
    else:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    if (i+str(j)) in c_list:
                        print('□',end='')
                    else:
                        print('■',end='')
                else:
                    if j==2 or j==8:
                        if (i+str(j)) in c_list:
                            print('□',end='   ')
                        else:
                            print('■',end='   ')
                    else:
                        if (i+str(j)) in c_list:
                            print('□',end='')
                        else:
                            print('■',end='')
                            
            print()
    print('입니다.')
    print()
    pe_c=int(input('몇 좌석을 예매하실건가요? (ex. 2자리가 예약하고싶으면 2 라고 입력)>> '))
    print()
    while pe_c>0:
        pe_c-=1
        reser_c=input('어떤 좌석을 예약하실건가요? (하나씩 입력) ex. A1 >>')
        if reser_c in c_list:
            rc+=1
            for i in range(100):
                if c_list[i]==reser_c:
                    break
                else:
                    pass
            c_list[i]= c_list[i]+'1'
            for i in seat:
                for j in range(1,11,1):
                    if j==1:
                         print(i,end=' ')
                         if (i+str(j)) in c_list:
                             
                             print('□',end='')
                        
                         else:
                             
                             print('■',end='')
                    else:
                        if j==2 or j==8:
                            if (i+str(j)) in c_list:
                                print('□',end='   ')
                            else:
                                print('■',end='   ')
                        else:
                            if (i+str(j)) in c_list:
                                print('□',end='')
                            else:
                                print('■',end='')
                print()
            
        else:
            print('예매할 수 없는 좌석입니다.')
            pe_c+=1

    while True:
        ccc=input('혹시 예매를 취소할 좌석이 있나요?')
        if ccc=='네':
            cccc=input('어느 좌석을 예매 취소할까요?')
            if cccc not in c_list:
                for i in range(100):
                    if (c_list[i])[0]+(c_list[i])[1]==cccc:
                        break
                    else:
                        pass
                c_list[i]=cccc

                for i in seat:
                    for j in range(1,11,1):
                        if j==1:
                             print(i,end=' ')
                             if (i+str(j)) in c_list:
                             
                                 print('□',end='')
                        
                             else:
                             
                                 print('■',end='')
                        else:
                            if j==2 or j==8:
                                if (i+str(j)) in c_list:
                                    print('□',end='   ')
                                else:
                                    print('■',end='   ')
                            else:
                                if (i+str(j)) in c_list:
                                    print('□',end='')
                                else:
                                    print('■',end='')
                    print()

                
                cc=input('예매를 취소할 좌석이 더 있나요?')
                if cc=='네':
                    continue
                elif cc=='아니요':
                    break
            else:
                print('예매되지 않은 좌석입니다.')
        elif ccc=='아니요':
            break
        


    reser_c1=input('추가로 예매할 좌석이 있으신가요? ')
    if reser_c1=='네':
        end=0
    elif reser_c1=='아니요':
        end=1
        print('프로그램을 종료하겠습니다.')
        
def d_seat():
    global rd,end
    if rd==0:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    print('□',end='')
                else:
                    if j==2 or j==8:
                        print('□',end='   ')
                    else:
                        print('□',end='')
            print()
        
    else:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    if (i+str(j)) in d_list:
                        print('□',end='')
                    else:
                        print('■',end='')
                else:
                    if j==2 or j==8:
                        if (i+str(j)) in d_list:
                            print('□',end='   ')
                        else:
                            print('■',end='   ')
                    else:
                        if (i+str(j)) in d_list:
                            print('□',end='')
                        else:
                            print('■',end='')
                            
            print()
    print('입니다.')
    print()
    pe_d=int(input('몇 좌석을 예매하실건가요? (ex. 2자리가 예약하고싶으면 2 라고 입력)>> '))
    print()
    while pe_d>0:
        pe_d-=1
        reser_d=input('어떤 좌석을 예약하실건가요? (하나씩 입력) ex. A1 >>')
        if reser_d in d_list:
            rd+=1
            for i in range(100):
                if d_list[i]==reser_d:
                    break
                else:
                    pass
            d_list[i]=d_list[i]+'1'
            for i in seat:
                for j in range(1,11,1):
                    if j==1:
                         print(i,end=' ')
                         if (i+str(j)) in d_list:
                             
                             print('□',end='')
                        
                         else:
                             
                             print('■',end='')
                    else:
                        if j==2 or j==8:
                            if (i+str(j)) in d_list:
                                print('□',end='   ')
                            else:
                                print('■',end='   ')
                        else:
                            if (i+str(j)) in d_list:
                                print('□',end='')
                            else:
                                print('■',end='')
                print()
            
        else:
            print('예매할 수 없는 좌석입니다.')
            pe_d+=1

    while True:
        ddd=input('혹시 예매를 취소할 좌석이 있나요?')
        if ddd=='네':
            dddd=input('어느 좌석을 예매 취소할까요?')
            if dddd not in d_list:
                for i in range(100):
                    if (d_list[i])[0]+(d_list[i])[1]==dddd:
                        break
                    else:
                        pass
                d_list[i]=dddd

                for i in seat:
                    for j in range(1,11,1):
                        if j==1:
                             print(i,end=' ')
                             if (i+str(j)) in d_list:
                             
                                 print('□',end='')
                        
                             else:
                             
                                 print('■',end='')
                        else:
                            if j==2 or j==8:
                                if (i+str(j)) in d_list:
                                    print('□',end='   ')
                                else:
                                    print('■',end='   ')
                            else:
                                if (i+str(j)) in d_list:
                                    print('□',end='')
                                else:
                                    print('■',end='')
                    print()

                
                dd=input('예매를 취소할 좌석이 더 있나요?')
                if dd=='네':
                    continue
                elif dd=='아니요':
                    break
            else:
                print('예매되지 않은 좌석입니다.')
        elif ddd=='아니요':
            break
  
            
    reser_d1=input('추가로 예매할 좌석이 있으신가요? ')
    if reser_d1=='네':
        end=0
    elif reser_d1=='아니요':
        end=1
        print('프로그램을 종료하겠습니다.')


def e_seat():
    global re,end
    if re==0:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    print('□',end='')
                else:
                    if j==2 or j==8:
                        print('□',end='   ')
                    else:
                        print('□',end='')
            print()
        
    else:
        print('현재 남아있는 좌석은')
        for i in seat:
            for j in range(1,11,1):
                if j==1:
                    print(i,end=' ')
                    if (i+str(j)) in e_list:
                        print('□',end='')
                    else:
                        print('■',end='')
                else:
                    if j==2 or j==8:
                        if (i+str(j)) in e_list:
                            print('□',end='   ')
                        else:
                            print('■',end='   ')
                    else:
                        if (i+str(j)) in e_list:
                            print('□',end='')
                        else:
                            print('■',end='')
                            
            print()
    print('입니다.')
    print()
    pe_e=int(input('몇 좌석을 예매하실건가요? (ex. 2자리가 예약하고싶으면 2 라고 입력)>> '))
    print()
    while pe_e>0:
        pe_e-=1
        reser_e=input('어떤 좌석을 예약하실건가요? (하나씩 입력) ex. A1 >>')
        if reser_e in e_list:
            re+=1
            for i in range(100):
                if e_list[i]==reser_e:
                    break
                else:
                    pass
            e_list[i]=e_list[i]+'1'
            for i in seat:
                for j in range(1,11,1):
                    if j==1:
                         print(i,end=' ')
                         if (i+str(j)) in e_list:
                             
                             print('□',end='')
                        
                         else:
                             
                             print('■',end='')
                    else:
                        if j==2 or j==8:
                            if (i+str(j)) in e_list:
                                print('□',end='   ')
                            else:
                                print('■',end='   ')
                        else:
                            if (i+str(j)) in e_list:
                                print('□',end='')
                            else:
                                print('■',end='')
                print()
            
        else:
            print('예매할 수 없는 좌석입니다.')
            pe_e+=1
    
    while True:
        eee=input('혹시 예매를 취소할 좌석이 있나요?')
        if eee=='네':
            eeee=input('어느 좌석을 예매 취소할까요?')
            if eeee not in e_list:
                for i in range(100):
                    if (e_list[i])[0]+(e_list[i])[1]==eeee:
                        break
                    else:
                        pass
                e_list[i]=eeee

                for i in seat:
                    for j in range(1,11,1):
                        if j==1:
                             print(i,end=' ')
                             if (i+str(j)) in e_list:
                             
                                 print('□',end='')
                        
                             else:
                             
                                 print('■',end='')
                        else:
                            if j==2 or j==8:
                                if (i+str(j)) in e_list:
                                    print('□',end='   ')
                                else:
                                    print('■',end='   ')
                            else:
                                if (i+str(j)) in e_list:
                                    print('□',end='')
                                else:
                                    print('■',end='')
                    print()



                
                
                ee=input('예매를 취소할 좌석이 더 있나요?')
                if ee=='네':
                    continue
                elif ee=='아니요':
                    break
            else:
                print('예매되지 않은 좌석입니다.')
            
        elif eee=='아니요':
            break
        
    reser_e1=input('추가로 예매할 좌석이 있으신가요? ')
    if reser_e1=='네':
        end=0
    elif reser_e1=='아니요':
        end=1
        print('프로그램을 종료하겠습니다.')







    
while end<1:

    answer_det=input('예매하실 영화가 있으신가요? >>')
    if answer_det=='아니요':
        print('프로그램을 종료하겠습니다.')
    else:
        answer_a=input('무슨 영화를 예매하실건가요?(ex.스턴트맨) >>')
        if answer_a=='스턴트맨':
            a_seat()
        elif answer_a=='범죄도시4':
            b_seat()
        elif answer_a=='쿵푸팬더4':
            c_seat()
        elif answer_a=='파묘':
            d_seat()
        elif answer_a=='남은 인생 10년':
            e_seat()
        else:
            print('상영중인 영화가 아닙니다.')
        
        
        
                                               

    
    


        
        
    






