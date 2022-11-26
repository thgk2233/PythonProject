'''
파일명 : Ex03-5-casting.py

casting
    변수에 유형을 지정하려는 경우 캐스팅으로 가능.
'''
# 정수형
x = int(1)
print(x)
y = int(2.8)
#int는 정수형이므로 int(소수점)일 때 뒤에 소수점자리의 데이터 소실
print(y)
z = int("3")
#"3"은 string 이였으나 int로 인해 정수취급으로 바뀜=> 3
print(type(z))

# 실수형
x = float(1)
print(x)
z = float("3")
print(z)

# 문자형
x = str(1)
y = str(2)
print(x)
print(x+y)
# 문자형이였기때문에 문자취급하여 더하기 셈을 하지 않고 문자값을 붙여서 출력.

#아스키코드 변환
a = ord('A')
print(a)
b = chr(65)
print(b)
