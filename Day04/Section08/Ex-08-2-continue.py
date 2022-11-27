'''
파일명 : Ex-08-2-continue.py

continue
    while문이나 for문과 같은
    반복문을 강제로 건너뛰기
    (아래코드는 실행하지 않는다)

'''
total = 0
for a in range(1, 101):
    if a % 3 ==0:
        continue
    print('a : {}, total{}'.format(a, total))
    total += a
print(total)