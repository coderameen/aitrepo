myn = 100#global variable
class StudentDetails:
    #instance varaible
    n = 20
    def myfunc(self):
        #local variable
        nl = 10
        print("This is my simple class function")

s1 = StudentDetails()
print(s1.n)
print(s1.myfunc())
# print(s1.nl)
print(myn)
s2 = StudentDetails()
