'''
파일명 : Ex02-7-set.py
Set
    순서가 없다=
    변경할 수 없다
    인덱싱되지 않는 컬렉션
    중복값 없다
'''
thisset = {"피카츄", "라이츄", "파이리"}
#실행할때마다 순서가 변경
print(thisset)
#항목 가져오기
for x in thisset:
    print(x)

#값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)

#항목 추가하기
thisset. add("꼬부기")
print(thisset)

# 다른 set 항목 추가
thisset1 = {"피카츄","라이츄","파이리"}
thisset2 = {"꼬부기","잠만보","뮤츠"}
thisset1.update(thisset2)
print(thisset1)
#중복값이 있으면 추가되지않음, 중복값 제거용으로도 사용가능

#항목제거
thisset = {"피카츄","라이츄","파이리"}
thisset.remove("피카츄")
print(thisset)
#thisset.remove("피카츄")
#print(thisset)

thisset = {"피카츄","라이츄","파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)
#remove는 중복값으로 계속 사용시 에러 , discard는 에러안남

#항목제거(무작위제거)
thisset.pop()

#비우기(전부)
thisset.clear()
print(thisset)
