# 생성자와 메소드
class Triangle :
    def setData(self, b, h) : #메소드
        self.b = b
        self.h = h

tri1 = Triangle() #객체 생성

# Triangle 도 분명히 함수형태인데 클래스 안에서는 이런 매소드는 정의되지 않음

# 생성자
# 객체 생성과 동시에 초깃값을 설정하는 메소드
# 기본 생성자는 클래스를 선언할 때 자동으로 만들어지며
# 객체를 만들 때 자동으로 실행
# 함수, 메소드, 생성자들의 관계
# 함수: 특정 기능의 집합
# 메소드: 클래스 안에 함수
# 생성자: 객체를 생성할 때 자동 호출

class Triangle :
    def setData(self, b, h) :
        self.b = b
        self.h = h
				
    def area(self) :
        return self.b * self.h / 2

tri1 = Triangle()
tri1.setData(4, 5)

tri2 = Triangle()
tri2.setData(6, 10)

print(tri1.b, tri1.h, tri1.area())
print(tri2.b, tri2.h, tri2.area())

# 삼각형 객체의 필드는 꼭 저장해야하는 값인데 객체를 생성할 때마다 매번 setData()를 실행
# 생성자를 사용해 코드를 좀 더 효율적으로 사용 가능
# 이름을 마음대로 설정할 수 있는 메소드와 달리 __init__ 이라는 이름을 사용
# setData()를 __init__ 형식으로 수정
class Triangle :
    def __init__(self, b, h) : #생성자
        self.b = b
        self.h = h
    
    def area(self) :
        return self.b * self.h / 2

   
tri1 = Triangle(4, 5) #호출하면서 바로 인자 전달
tri2 = Triangle(6, 10)

print(tri1.b, tri1.h, tri1.area())
print(tri2.b, tri2.h, tri2.area())

# 정적 메소드, 인스턴스 메소드, 클래스 메소드
# 지금까지 사용한 메소드는 정화히 표현하자면인스턴스메소드
# 인스턴스 메소드는 self로 인스턴스의 필드에 접근하는 메소드
# 위 예시에서 area() 메소드는 self 메소드는 self를 매개변수로 인스턴스의 필드에 접근하여
# 인스턴스 변수를 가져와 넓이 연산을 실행

#반면, 인스턴스의 필드에 접근하지 않아 self 매개변수를 갖지 않는 메소드를 정적 메소드라고 함
# 정적 메소드는 클래스 안에서 선언되고 인스턴스로 실행하지만 일반 함수 같이 사용 가능
# 클래스 안에서 메소드 선언 앞에 @staticmethod 라고 표시해야만 정적 메소드로 인식하며
# 인스턴스 필드에 접근할 수 없게 되고
# 이를 표시하지 않으면 인스턴스 메소드로 인식되어 
# self 로 인스턴스 필드에 접근할 수 있다는 점을 다시 한번 확인해야 함



class Triangle : 
    cal_count = 0
    
    def __init__(self, b, h = 5) :
        self.b = b
        self.h = h
        
    def area(self) :
        Triangle.cal_count += 1
        
        return self.b * self.h / 2
    
    @staticmethod
    def isIsosceles(a, b) :
        Triangle.cal_count += 1
        return a == b    
   
tri1 = Triangle(4) #밑변 4 삼각형 객체 생성

print(tri1.b, tri1.h, tri1.area(), tri1.cal_count)
print(tri1.isIsosceles(5,5), tri1.cal_count)
print(Triangle.isIsosceles(5,4))


# 클래스 메소드도 정적 메소드의 접근 방식과 마찬가지로 클래스로 직접 접근이 가능


class Triangle : 
    cal_count = 0
    
    def __init__(self, b, h = 5) :
        self.b = b
        self.h = h
        
    def area(self) :
        Triangle.cal_count += 1
        
        return self.b * self.h / 2
    
    @staticmethod
    def isIsosceles(a, b) :
        Triangle.cal_count += 1
        return a == b
    
    @classmethod
    def printCount(cls) :
        print(cls.cal_count)
   
tri1 = Triangle(4) #밑변 4 삼각형 객체 생성

print(tri1.b, tri1.h, tri1.area(), tri1.cal_count)
print(Triangle.isIsosceles(5,4))

tri1.printCount() #인스턴스로 접근
Triangle.printCount() #클래스로 직접 접근