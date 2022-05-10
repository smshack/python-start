# 함수의 구성요소인 매개변수와 반환값은 항상 꼭 포함되어야 하는 것이 아니라
# 필요에 따라 생략 가능
def guide() : #매개변수 X, 반환값 X
    print("두 정수를 입력받아 곱한 결과를 출력하는 프로그램입니다.")
    
def inputnums() : #매개변수 X, 반환값 O
    a = int(input("첫번째 정수를 입력하세요:"))
    b = int(input("두번째 정수를 입력하세요:"))
    return a, b

def multi(num1, num2) : #매개변수 O, 반환값 O
    return num1 * num2
    
def printResult(result) : #매개변수 O, 반환값 X
    print("두 수의 곱셈 결과는 %d입니다." %result)
    
guide()
n1, n2 = inputnums() #반환 값이 두 개이니 두 변수에 초기화
res = multi(n1, n2)
printResult(res)

# 매개변수
# 필요한 입력값을 선언하고
# 전달 인자로 함수 사용시 받음

def recArea(a, b) : #사각형의 넓이를 연산하고 반환하는 함수
    return a * b 

print(recArea(10, 20))


def subNums(a, b) :
    return a - b

num = 13
# 파이썬은 함수를 호출할 때 매개변수를 지정하여 인자를 전달 가능
print(subNums(b = 20, a = num))

# 매개변수의 개수는 제항 없이 입력 가능 ,
# 호출할 때 매개변수와 같은 수의 전달 인자를 입력해야함
def sumSevenNums(a, b, c, d, e, f, g) :
    return a + b + c + d + e + f + g 
   
def sumThreeNums(a, b, c) :
    return a + b + c

print(sumSevenNums(1, 3, 4, 2, 3, 4, 5))
print(sumThreeNums(1, 5, 10))

# 위에 두 함수는 동일한 기능을 수행하지만 매개변수만 다른 함수는 가변인자 함수로 선언 가능
# 매개변수 앞에 * 만 입력하여 생성 가능
# def 함수이름(*매개변수):
def subNums(*t) :
    print(t, type(t)) #튜플인지 확인
    total = 0
    
    for i in t :
        total = total + i
    
    return total

print(subNums(1, 5, 32, 3, 4, 57, 5))
print(subNums(5, 29))

# 필요에 따라 가변인자와 일반 매개변수를 같이 사용 가능
def calNums(ch, *t) :
    if ch == "sum" : #모든 값을 더합니다.
        total = 0
        for i in t :
            total = total + i

    elif ch == "mul" :	#모든 값을 곱합니다.
        total = 1
        for i in t :
            total = total * i

    else :
        print("실행할 수 없습니다.")
        
    return total
    
choice = input("덧셈은 sum, 곱셈은 mul를 입력하세요:")
print(calNums(choice, 1, 2, 3, 2, 5, 3, 2))  

# 키워드 매개변수
# 매개변수 앞에 ** 을 입력하면 함수 호출 시 전달 인자를 (key1=value,key2=value2 ...) 형식으로 입력
# 딕셔너리 형태로 선언 가능
def func(**kwargs) :
    print(kwargs)
    
num = 10
func(apple="사과", a = num, num = 4)

def func(*nums, **kwargs) :
    print(nums)
    print(kwargs)
    
num = 10
func(1, 3, 5, 7, apple="사과", a = num, num = 4)


## 주의할 점은 키워드 형태의 인수 뒤에 키워드 형태가 아닌 인수는 올수 없음
