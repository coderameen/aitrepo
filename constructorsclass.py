class Student:
    #constructor
    def __init__(self):
        self.usn = "01"
        self.name = "bob"
        self.addr = "banglr"
    def student_details(self):
        print(f"The student USN: {self.usn} | Name is {self.name} and the address is {self.addr}")
obj = Student()
print(obj.student_details())
        