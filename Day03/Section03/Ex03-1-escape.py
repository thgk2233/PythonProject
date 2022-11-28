'''
파일명 : Ex03-1-escape.py

escape 문자 (\: 엔터위에 단축키, 우리가 흔히 쓰는 돈단위 원 표시모양)

    \n -> 줄바꿈
    \t -> 탭
    \b -> 백스페이스, 한칸 앞을 지운다.
    \a -> 벨
    \\ -> 백슬레쉬, "\를 문자열(str)로 바꾼다"
    \' -> 작은 따옴표
    \" -> 큰 따옴표
    \r -> 줄 바꿈. 커서를 앞으로 이동
    \f-> 줄 바끔. 커서를 다음 줄로 이동
    raw string - > escape 문자의 의미무시
        ex)print(r'hello data\nhello data') -> hello data\nhello data 로 출력
'''

print('Hello,\'world\'')
print("Hello\"World\"")
print('Hello,\'world\'')
print("Hello\"World\"")
