"""
직접 타이핑하는 것은 타이핑의 장점이 아니다.

리스트 기반으로 만들었을 때
딕셔너리 기반으로 만들었을 때
클래스 기반으로 만들었을 때
"""
class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._number)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._number)

student1 = Student('Kim',1,1,{'gender': 'Male', 'score1': 95, 'score2': 95})  
student2 = Student('Lee',2,2,{'gender': 'Female', 'score1': 95, 'score2': 95})  
student3 = Student('Park',3,4,{'gender': 'Male', 'score1': 95, 'score2': 95})  
        
print(student1)
print(student1.__dict__)
print(student1.__weakref__)
student1.__weakref__ = 's'

