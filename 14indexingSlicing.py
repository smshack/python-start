# 아스키 코드 값
print(ord("A"))
print(chr(65))


# 인덱싱
str = "apple"
print("str의 첫 번째 문자는", str[0], "네 번째 문자는", str[3])

a = "Hello goorm!"
b = a[4] + a[5] + a[6]
print(a[0], a[1], a[2], a[3], a[4])
print(b)

# 파이썬에서 인덱스는 앞에서 뿐 마이라 뒤에서부터 역시 접근 가능
# 뒤에서 부터 -1 부터 시작

a = "Hello goorm!"
b = a[-1] + a[-2] + a[-3]
c = a[-0]
print(b)
print(c)

# 슬라이싱
# 지정 범위 만큼 데이터 요소를 잘라내는 기능
# 변수명[첫 인덱스 번호: 마지막 인덱스 번호]

a = "Hello goorm!"
b = a[0:5]
print(b)


a = "Hello goorm!"

b = a[:5]
c = a[5:]
print(b)
print(c)


a = "Hello goorm!"

b = a[0:-5]
c = a[6:-11]
print(b)
print(c)