class Student:
    def __init__(self):
        self.__marks = 90     

    def showMarks(self):
        print("Marks =", self.__marks)

s = Student()

s.showMarks()

