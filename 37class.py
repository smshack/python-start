# 클래스와 클래스 구성요소, 상속
# 객체 지향 언어가 지닌 최고의 무기 

# 스코프를 어떻게 하느냐에 따라 내용과 깊이가 달라짐
# 클래스는 언어를 나누는 기준인 중요한 용법
# 삼각형의 밑변과 높이 값을 이용해 넓이를 구하는 프로그램을 생성

# 함수로 생성
def calArea(b, h) :
    return b * h / 2

triangle1_b = 20
triangle1_h = 10

triangle2_b = 12
triangle2_h = 6

triangle3_b = 5
triangle3_h = 30

print(calArea(triangle1_b, triangle1_h))
print(calArea(triangle2_b, triangle2_h))
print(calArea(triangle3_b, triangle3_h))

## 삼각형 처럼 연산의 중심이 되는 것을 객체
# 함수라는 틀을 만드는 것처럼 객체도 세부 정보만 조금씩 다르게 지정해 만들 수 있도록 틀을 생성 가능
# 객체를 지정하고 말하면 객체라고 표현하고 그 객체를 생성한 클래스와의 관계를 얘기 하면 인스턴스라고 함

# Triangle  라는 클래스 선언
# pass는 실행할 내용이 없을 때 지나치라는 명시적 역할을 합
# 조건문이나 반복문에도 똑같이 사용 가능
# 만들어 놓은 클래스로 객체를 생성하기 위해서는 위 예시 코드와 같이 객체 이름 = 클래스 () 형식으로 생성
# 아무런 정보 없이 삼각형 클래스를 이용해 삼각형 객체 네개를 생성
class Triangle :
	pass

tri1 = Triangle()
tri2 = Triangle()
tri3 = Triangle()
tri4 = Triangle()

# 클래스 변수
# 클래스에서도 변수를 이용해 값을 저장하며, 클래스에서는 클래스 변수와 인스턴스 변수를 사용할 수 있음
# 클래스 변수는 클래스 안에서 선언된 변수,
# 즉 객체가 아닌 클래스에 종속된 변수
# 클래스 변수는 같은 클래스로 만들어진 인스턴스끼리 공유하고 접근이 가능한 변수이기에 어떤 객체에서 선언하더라도 동일한 값이 담겨 있는 것을 볼수 있음

# 클래스 변수를 선언
# 클래스를 정의할 때 그 범위 안에 변수를 정의해주면 됨
# 선언한 객체로 클래스 변수를 접근하려면 객체이름, 변수이름 형식으로 작성
# 출력 결과를 보면 위 2개 값과 아래 2개 값이 동일한 순서로 출력됨
class Triangle :
	height = 10
	bottom = 4

tri1 = Triangle()
print(tri1.height)
print(tri1.bottom)

tri2 = Triangle()
print(tri2.height)
print(tri2.bottom)

# 메소드는 클래스 안에서 어떠한 기능을 수행하는 함수로
# 이를 이용해객체 정보를 지정할 수 있음
# 사용자가 전달 인자를 입력하지 않는 매개변수 self를 사용
class Triangle :
    def setData(self, b, h) : #메소드
        self.b = b
        self.h = h

tri1 = Triangle() #객체 생성
tri1.setData(4, 5) #객체 메소드 실행
print(tri1.b, tri1.h)

# self.변수이름 형식으로 객체의 필드에 저장한 변수는 tri1.b 와 같은 형식으로 해당 값에 접근하고 가져올 수 있음
# 인수턴스 변수는 각 객체의 고윳값이기 때문에 각기 다른 객체끼리 공유되지 않으며, 클래스 또한 인스턴스 변수에 접근하고자 할 때
# self 없이 변수 이름만으로 접근할 수 없음

class Triangle :
    def setData(self, b, h) : #메소드
        self.b = b
        self.h = h
    
    def area(self) : #def area() : 불가능
        return self.b * self.h / 2 #
   
tri1 = Triangle() #객체 생성
tri1.setData(4, 5) #객체 메소드 실행

tri2 = Triangle() #객체 생성
tri2.setData(6, 10) #객체 메소드 실행

print(tri1.b, tri1.h, tri1.area())
print(tri2.b, tri2.h, tri2.area())

## 각각 tri1, tri2라는 객체를 생성하고 setData()메소드를 통해 b,h 값을 입력
class Triangle :
    def setData(self, b, h) : #메소드
        self.b = b
        self.h = h
    
    def area(self) : #def area() : 불가능
        return self.b * self.h / 2 #
   
tri1 = Triangle() #객체 생성
tri1.setData(4, 5) #객체 메소드 실행

tri2 = Triangle() #객체 생성
tri2.setData(6, 10) #객체 메소드 실행

print(tri1.b, tri1.h, tri1.area())
print(tri2.b, tri2.h, tri2.area())

## 클래스 변수와 인스턴스 변수의 비교
class Triangle : 
    cal_count = 0
    
    def __init__(self, b, h = 5) : #생성자
        self.b = b
        self.h = h

    def area(self) :
        Triangle.cal_count += 1
        
        return self.b * self.h / 2

tri1 = Triangle(4)
tri2 = Triangle(6, 10)

print(tri1.b, tri1.h, tri1.area(), tri1.cal_count)
print(tri2.b, tri2.h, tri2.area(), tri2.cal_count)

print(Triangle.cal_count)
# 만약 area() 메소드에서 cal_count라고만 작성했다면 지역변수로 인식되어 오류가 발생
# 함수 안에서 전역 변수 값을 함부로 대입, 교체할 수 없게 함
# 클래스 변수는 모든 객체가 공유하기 때문에 trai.cal_count형식으로 접근 가능
# 해당 예제에서 인스턴스 변수 사용 또한 눈여겨 봐야 함