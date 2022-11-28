'''
파일명 : Ex 03-2-print.py
print() 함수 사용법
    sep : 출력할 value의 구분문자,값사이에 공백이 아닌 다른 문자를 넣고 싶을때 사용
          구분자라는 separator에서 따옴
    end : value 출력 후 출력할 문자 ( print 뒤의 기본값 '\n', (\n 은 줄바꿈의 제어문자))
    file : 출력방향 지정


'''

print("재미있는", "파이썬")
print("python", "JAVA", "C", sep=',')

print("안녕", end=' ')
print("하세요")

fos = open('sample.py', mode = 'wt')
#wt = write text mode
#파일을 sample.py라는 이름으로 write text mode 지정
print('print("Hello World")', file=fos)
#fos라고 지정한 파일방향으로 hellow world를 print 하겠다
fos.close()

