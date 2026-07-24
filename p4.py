class Student:
    def __init__(self):
        self.__marks = 90     # Private variable

    def showMarks(self):
        print("Marks =", self.__marks)

s = Student()

s.showMarks()

# print(s.__marks)   # Error