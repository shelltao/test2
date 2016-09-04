# coding:utf-8


# bussise.py:
def main():
    with open('settings') as f:
        target = f.read().strip()

    factory = Factory.create(target)


class Factory(object):
    name = 'test'

    def hello(self):
        print 'hello'

    @staticmethod
    def create(human_type):
        if human_type == 'teacher':
            return Teacher
        elif human_type == 'student':
            return Student
        elif human_type == 'chief':
            return Chief

    @classmethod
    def instance(cls):
        cls.name


Human = Factory.create('teacher')
human = Human('renlei')


class Student(object):
    def __init__(self, name):
        self.name = name

    def speak(self, words):
        print self.name, 'say', words

    @staticmethod
    def run():
        print 'run'

    @classmethod
    def run2(cls):
        print 'run'


class Teacher(object):
    def __init__(self, name):
        self.name = name

    def question(self, student_name):
        print self.name, 'ti wen,', student_name, 'qinghuida'

        student = Student(student_name)
        student.speak('俺不会')

        Student.run()


# chief.py

class Chief(object):


if __name__ == '__main__':
    student = Student('昌辉')

    teacher = Teacher('培武')

    student.speak('大家好')

    teacher.question(student)
