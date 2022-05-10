# 전역변수
# 코드 전체에서 사용할 수 있는 변수

# 지역 변수
# 정해진 범위에서만 사용 가능한 변수

num = 3 #전역 변수 num 선언
globallist = [] #전역 변수 globallist 선언

def mulNum(a) : #지역 변수 a 선언
    a = a * num
    globallist.append(3)
    return a #a 소멸

def subNum(a) : #지역 변수 a 선언
    a = a - num
    print(a) #a 소멸

res = mulNum(4) #전역 변수 res 선언
print(res)

subNum(7)
print(num)
print(globallist) #프로그램 종료, 전역 변수 num, res, globallist 소멸