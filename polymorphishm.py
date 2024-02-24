#overloading
'''
1.operator ol
'''
# print(10 + 30)
# print('hello'+'ait')

# l = [10,20,30]
# print(l*3)

# print(10*3)

'''
2.Mehtod ol
'''

# def add():
#     return 10+20

# print(add())

# def add(a,b):
#     return a+b
# print(add(10,30))

# def add(a,b,c):
#     return (a+b+c)

# print(10,20,30)

# def add(a,b=10):
#     print(a+b)
# add(10)


#Method overriding
class Parent:
    def display(self):
        print("This is parent parament")

class Child(Parent):
    def display(self):
        super().display()
        print("This is child property")
c = Child()
c.display()