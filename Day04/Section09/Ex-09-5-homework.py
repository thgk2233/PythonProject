'''
[회원가입]
아이디를 입력하세요(3글자 이상) >>>
> 3글자 이상 입력해주세요!

아이디를 입력하세요(3글자 이상) >>>

패쓰워드를 입력하세요(영문 숫자 포함 8자이상) >>>
>영문 숫자 포함 8자 이상 입력해주세요

패쓰워드 확인 한번 더 입력하세요 >>>
>일치하지 않습니다.


패쓰워드를 입력하세요(영문 숫자 포함 8자이상) >>>

패쓰워드 확인 한번 더 입력하세요 >>>
>
회원가입 완료!



[로그인]

아이디를 입력하세요>>>
>아이디가 일치하지 않습니다.

아이디를 입력하세요>>>

패쓰워드를 입력하세요>>>
>패쓰워드가 일치하지 않습니다.

패쓰워드를 입력하세요>>>

로그인성공
ID님 환영합니다.


'''

while True:
    ID = input('아이디를 입력하세요(3글자 이상) >>> ')
    ch_count = 0
    num_count = 0
    for ch in ID:
        if ch.isalpha():
        # .isalpha는 bool(true or false),알파벳이 맞느냐 물어보는 method
            ch_count += 1
        elif ch.isnumeric():
            num_count += 1
    if ch_count + num_count > 3:
        print('가능한 아이디입니다!')
        while True:
            pwd = input('패쓰워드를 입력하세요(영문 숫자 포함 8자이상) >>> ')
            ch_count = 0
            num_count = 0
            for ch in pwd:
                if ch.isalpha():
                    ch_count += 1
                elif ch.isnumeric():
                    num_count += 1
            if ch_count + num_count > 8 and ch_count > 0 and num_count > 0:
                while True:
                    pwd2 = input('패쓰워드 확인을 위해 한번더 입력해주세요 >>> ')
                    if str(pwd) == str(pwd2):
                        print('회원가입완료')
                        break
                    else:
                        print('비밀번호가 맞지않습니다.')
                break
            else:
                print('영문 숫자 포함 8자 이상 입력해주세요')
        break
    else:
        print('3글자 이상 입력해주세요!')
