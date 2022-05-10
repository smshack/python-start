# 함수의 역할 
"""
지정기능을 실행하는 단위
코드의 가독성과 프로그램의 효율성 증대

사용자가 만든 함수에 인자를 전달하면 연산 결과가 반환
# 함수 정의
def 함수이름(매개변수1 , 매개변수2 ...) :
    실행 구문
    ...
    return 반환값

# 함수 호출
함수 이름(전달인자1, 전달인자2)
"""

#함수 선언
def plusThree(num) :
    return num + 3

#함수 호출
result = plusThree(10)

print(result)

# 학생의 주민등록 번호를 앞자리에서부터 일곱 자리까지 입력하면
# 나이, 생일 , 성별을 자동으로 계산하여 반환하는 함수
# 함수 선언
#함수 선언
def stdInfo(rrn) :
    if int(rrn[6]) == 3 or int(rrn[6]) == 4 :
        biryear = int(rrn[0]+rrn[1]) + 2000
    else :
        biryear = int(rrn[0]+rrn[1]) + 1900
    
    age = year - biryear + 1
    birmonth = int(rrn[2] + rrn[3])
    birday = int(rrn[4] + rrn[5])
    
    if rrn[6] == "2" or rrn[6] == "4" :
        gen = "여자"
    else :
        gen = "남자"
        
    return [age, birmonth, birday, gen] #리스트 형식으로 반환

year = 2018
stdlist = []

stdrrn = input("학생의 주민등록번호를 7자리 입력하세요:")

stdlist.append(stdInfo(stdrrn)) #함수 호출

print(stdlist[0])

"""
코드의 가독성과 프로그램의 효율성 증대
프로그래밍에서 설계가 상당히 중요함

함수는 특정 기능을 위해 만든 여러 문장을 묶어서 실행하는 코드 블록 단위

이때 중요한 것은 함수의 이름
"""
a = 5
b = 10
print(a + b)

c = 34
d = 5
print(c + d)

e = 34
f = 10
print(e + f)

def printSum(a, b) :
    print(a+b)
    
printSum(5, 10)
printSum(34, 5)
printSum(34, 10)