"""
Chapter01-3
파이썬 심화
클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

기본 인스턴스 메소드
"""

class Student(object):
    """
    Student Class
    Author : Park
    Date : 2020.01.10
    Description : Class, Static, Instance Method
    """

    # Class Variable
    tuition = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self): #첫번째 인자로 self가 들어가면 인스턴스 메소드
        return '{}{}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}{}{}'.format(self._id,self.full_name(),self._email)
    
    #
    def get_fee(self):
        return ' Before Tuition -> Id : {}. fee : {}'.format(self._id, self._tuition)

    def get_fee_culc(self):
        return 'After tuition -> Id:{}{}'.format(self._id, self._tuition * Student.tuition)
        
    def __str__(self):
        return 'Student Info -> name : {} grade: {} email: {}'.format(self.full_name(), self._grade, self._email)

    #Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return  
        cls.tuition_per = per
        print('succeed! tuition increased!')


    # Class Method 로 정의하는 것을 권장
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition* cls.tuition_per, gpa)

    # Static Method
    @staticmethod 
    #사실 클래스나 인스턴스 메소드로 할 수 있다. 3가지 메소드가 있다는 것만 확인. 요즘에는 사용 x 
    #개인적으로 클래스와 연관이 있으면 클래스에 정의하는 것이 나음
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipent'.format(inst._last_name)
        return 'sorry'

student_1 = Student(1, 'kim', 'sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'lee', 'ingi', 'student2@naver.com', '2', 320, 3.4)

print(student_1)
print(student_2)

print(student_1.get_fee())
print(student_2.get_fee())

print()

# 학비 인상(클래스 메소드 미사용)
Student.tuition = 1.0


Student.raise_fee(1.5)

print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

#pythonic PEP


# 클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3,'park','minji','student3@gmail.com','3',550,4.5) # init에 붙히는 것보다 훨씬 직관적

print(student_3.detail_info())
print(student_3._tuition)

# 장학금 혜택 여부(스테이틱 메소드 미사용) # 클래스의 정보를 활용하는 메소드,  cls, self 인자도 필요없는 메소드
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipent'.format(inst._last_name)
    return 'sorry'

#그냥 호출
print(is_scholarship(student_3))
#클래스로 호출
print(Student.is_scholarship_st(student_3))

#인스턴스로 호출
print(student_2.is_scholarship_st(student_3))

