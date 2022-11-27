'''
파일명 : Ex05-1-if.py

조건문
    특정 조건을 만족하는지 여부에따라
    실행하는 코드가 달라야 할때 사용한다.
    !들여쓰기를 사용하여 코드의 범위 정의.!

    1.방법
    if(조건식) :
        (조건식이 참)실행할 코드

    2.방법
    if(조건식) :
        (조건식이 참)실행할 코드
    else(조건식) :
        (조건식이 거짓)실행할 코드

    3.방법
    if(조건식1) :
        (조건식1이 참)실행할 코드
    elif(조건식2):
        (조건식2이 참)실행할 코드
    else(조건식) :
        (조건식이 거짓)실행할 코드

'''

#if(조건식)
a = 7
b= 100
if b > a :
    print('b는 a보다 크다')
#True일 때 코드 실행.

#if(조건식) else
a = 7
b = 4
if b >= a:
    print("b는 a보다 크거나 같다")
else:
    print("b는 a보다 작다")

#if(조건식1) elif(조건식2) else
b = 3
if b==1:
    print("1")
elif b==2:
    print("2")
elif b==3:
    print("3")
else: #필요없음 else 생략가능
    print("1,2,3 아니다")
    #조건식을 여러개 쓰고 싶을 때 elif 사용
#