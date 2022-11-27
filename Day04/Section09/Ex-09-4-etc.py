'''
내장함수 보충
'''
result = format(10000) #str(10000) 과 같다
print(type(result))
result= format(10000, ',') #천단위 쉼표
print(result)

#abs=절대값
result = abs(10)
print(result)
result  = abs(-10)
print(result)

#max() 최대값 반환
#min() 최소값 반환
result = max(1,10)
print(result)
li = [5, 3, 4, 2, 1]
result = max(li)
print(result)
result = min(li)
print(result)

#pow() 거듭제곱 함수
result = pow(10, 2)
print(result)

# sorted() 함수 - 정렬
my_li = [5, 6, 3, 4, 1, 2]
result = sorted(my_li)
print(result)

print(result[0])
result = sorted(my_li, reverse=True)
print(result)

#zip()함수 (튜플로 묶어줌)
names = ['james', 'emily', 'amanda']
scores = [20, 70, 80]
for student in zip(names, scores):
    print(student)

names = ['james', 'emily', 'amanda']
scores = [20, 70, 80]
for name, score in zip(names, scores):
    print('{}의 점수는 {}점입니다.'.format(name, score))
