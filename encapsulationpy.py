class MyClass:
    # n = 10#public variable
    __n = 1000#protected variable
    def myfunc(self):
        print(self.__n)
        print("This is my local function")

obj = MyClass()
# print(obj.__n)
obj.myfunc()