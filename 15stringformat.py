city = "seoul"
today = 12
day = "화요일"
temperature = 26
announcement = "%s의 %d일 %s 기온은 %d도 입니다." %(city, today, day, temperature)
	
print("%s의 %d일 %s 기온은 %d도 입니다." %(city, today, day, temperature)) #1번 방법
print(announcement) #2번 방법


name = "goorm"
age = 25
height = 181.523456

print("저의 이름은 %s입니다." %name)

print("저는 %d살입니다." %25)
print("제 나이는 %d살입니다." %age)
print("제 나이는 %s살입니다." %age)
print("제 나이는 %.2f살입니다." %age)

print("저의 키는 %fcm입니다." %height)
print("저의 키는 %.2fcm입니다." %height)
print("저의 키는 %dcm입니다." %height)

print("저의 성은 '%c'입니다." %"남")

print("저의 나이는 16진수로 표현하면 %x, 8진수로 표현하면 %o입니다." %(age, age))

print("%10d %010d" %(10, 10))
	
#'김구름'을 포함하여 8칸의 공간 발생 -> 공백 5칸 + 김구름 3칸
print("%8s %8d %8s" %("김구름", 6, "컴퓨터공학"))
print("%-8s %-8d %-8s" %("김구름", 6, "컴퓨터공학"))

name1 = "김구름"
name2 = "박에듀"
age = 25
height = 181.123

# 인덱스 값 바로 대임 .format 함수 사용
print("저의 이름은 {2}입니다. 그리고 나이는 {1}살이고 키는 {0}cm입니다.".format(height, age, name1))
print("{1}의 나이:{0}, {2}의 나이: {0}".format(age, name1, name2))

# 변수 이름으로 대입
print("저의 이름은 {1}입니다. 그리고 나이는 {age}살이고 키는 {0}cm입니다. 제 가장 친한 친구는 {name}입니다.".format(181.12, "김구름",height = 181.123, age = 25, name = "박에듀"))


print("{length: >10d}".format(length = 30))
# 공백문자: (공백) ,정렬: 오른쪽 정렬, 폭: 10
# 순서대로 입력해야하고 생략 가능

print("{0:0^10}".format("goorm"))
# 공백문자: 0 ,정렬: 가운데 정렬, 폭: 10
# 순서대로 입력해야하고 생략 가능

print("{height:!>13.2f}".format(height = 181.24363))
# 공백문자: ! ,정렬: 오른쪽 정렬, 폭: 13, 소수점 2자리 표시
# 순서대로 입력해야하고 생략 가능
name = "김구름"
age = 25
height = 181.123
print(f"저의 이름은 {name}입니다. 그리고 나이는 {age+10}살이고 키는 {height:!^10.2f}cm입니다.")