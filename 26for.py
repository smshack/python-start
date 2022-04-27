# 반복문
# 데이터로 어떠한 기능을 수행하는 프로그램을 만들기 위한 용법이 필요
# 프로그램에서 어떻게 반복문을 잘 활용할 수 있는지
# 사전 검색 프로그램

## 1. 단어: 뜻 의 형식으로 딕셔너리를 초기화
## 2. 사용자에게 단어를 입력 받음
## 3. 사용자가 입력한 단어가 딕셔너리의 key면 value를 츌력함

count = 0
while count != 100:						#while범위시작
    print("Hello goorm!",count)
    count += 1							#while범위끝

engdic = {
    "apple" : "사과",
    "book" : ["책", "예약하다"],
    "grape" : "포도",
    "while" :"~하는동안에"
}

inputword = input("검색할 영어 단어를 입력하세요:")

print(engdic[inputword])

#콘솔 입력으로 문자열을 받은 뒤 정수로 변환
inputnum = int(input("양의 정수를 입력하세요:"))
num = 0

while num < inputnum:
    print("Python", num)
    num += 1

for i in range(0, 10, 1):
    print(i)

i = 0

while i < 10 :
    print(i)
    i += 1

for num in range(10) :
    print(num)
    
for a in range(4, 8) :
    print("<%d>" %a)


# 반복문의 중첩
for i in range(3) :
    for j in range(5) :
        print(i,j)
