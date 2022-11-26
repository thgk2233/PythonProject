'''
파일명 : EX02-8-dict.py

dictionary
    key:value 로 이루어져 쌍으로 데이터 값으로 저장하는데 사용

'''

# dictionary 선언
'''
키 이름을 사용하여 참조할 수 있다
'''
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}
print(thisdict)

#값가져오기
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}

print(thisdict["brand"])
print(thisdict.get("model"))
'''
get이라는 함수를 통해 method로 dictionary를 가져올 수 있음
thisdict.을 통해 각종 함수를 불러올 수 있음
'''

# 키 목록 가져오기
print(thisdict.keys())

# 추가하기
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict. update({"bgColor" : "black"})
print(thisdict)

# 변경하기
thisdict["color"] = "yellow"
thisdict.update({"bgColor" : "blue"})
print(thisdict)

#제거하기
thisdict.pop("model")
print(thisdict)

# 마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)