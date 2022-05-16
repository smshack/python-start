# 클래스 상속
# 클래스는 처음 프로그래밍을접하는 분에게는 생소하고 여려운 개념
# 클래스는 프로그램의 규모가 커지면서 자주 사용해야할 특정 객체를 좀더 쉽게 다루기 위해 사용
# 프로그램을 확장하다 보면 같은 종류의 다양한 객체를 추가할 수 있음
# 예를 들어 도형이라는 종류 아래에 속한 삼각형
# 원, 사각형, 또 그 아래 속하는 이등변 삼각형, 정삼각형과 같은 형식

# 공통된 속성을 가지고 있는 부분 정의하고 
# 그 부분을 상속해서 하위 클래스가 공통적으로 사용하는 개념
"""
class 부모클래스:
    ...
class 자식클래스(부모클래스):
    ...
"""
# 클래스에서 상속은 필수 기능
# 상속을 받는 자식 클래스는 부모 클래스의 메소드와 변수를 가져와 사용 가능
# 또한 필요에 따라 메소드를 재정의(오버로딩)할 수 있음

import math

#도형
class Shape :
    cal_count = 0
    figure = "Shape"

    @classmethod
    def class_printFigure(cls) :
        return cls.figure
    
    @staticmethod
    def static_printFigure() :
        return Shape.figure

#도형 상속 삼각형
class Triangle(Shape) : 
    figure = "triangle"
    
    def __init__(self, b, h=5) :
        self.b = b
        self.h = h
        
    def area(self) :
        Shape.cal_count += 1
        
        return self.b * self.h / 2

#도형 상속 정삼각형
class EquTriangle(Triangle) : 
    figure = "equilateral triangle"
    
    def __init__(self, b) :
        self.b = b
        
    def area(self) :
        Shape.cal_count += 1
        
        return 0.25 * math.sqrt(3) * self.b ** 2
    
    def circumference(self) :
        return self.b * 3

#도형 상속 원
class Circle(Shape) :
    figure = "circle"
    
    def __init__(self, r) :
        self.r = r
        
    def area(self) :
        Shape.cal_count += 1
        
        return math.pi * self.r ** 2
    
    def circumference(self) :
        return 2 * math.pi * self.r

tri = Triangle(10, 4)
eqtri = EquTriangle(3)
cir = Circle(8)

print(cir.static_printFigure(), cir.area(), cir.circumference())
print(tri.class_printFigure(), tri.area(), cir.circumference())
print(eqtri.class_printFigure(), eqtri.area(), cir.circumference())

print(Shape.cal_count, cir.cal_count, tri.cal_count)



# 클래스의 심화 개념
## 객체지향 프로그래밍에서 클래스는 다형성의 특징을 가짐

# 다중상속
# 파이썬은 부모 클래스를 어러개 상속할 수 있음

class First :
    name = "first"
    def __init__(self) :
        print("First class")
    
    def printFirst(self) :
        print("first")
        
class Second :
    name = "second"
    def __init__(self) :
        print("First class")
    
    @classmethod
    def printName(cls) :
        print(cls.name)

#상속해야 할 부모클래스가 두 개인 경우 충돌 가능
#파이썬은 MRO에 따라 다중 상속을 진행
# 상속을 명시한 클래스 목록 중에 왼쪽에서 오른쪽 순서로 메소드를 찾음
class Third(First, Second) :
    pass

third = Third()
third.printName()
third.printFirst()

#오버로딩은 지원 하지 않음

## 오버라이딩: 상속 받는 클래스에서 부모 클래스의 메소드를 재정의하는 것
## 오버로딩: 한 클래스 안에서 같은 이름의 메소드를 여러번 선언하는 것

class First :
    name = "first"
    
    def __init__(self) :
        print("First class")
    
    def printFirst(self) :
        print("first1")
        
    def printFirst(self) :
        print("first2")
                
class Second :
    name = "second"
    
    def __init__(self) :
        print("First class")
    
    @classmethod
    def printName(cls) :
        print(cls.name)
    
class Third(First, Second) :
    pass

third = Third()
third.printName()
third.printFirst()


