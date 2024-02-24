# #single level inheritence
# class Parent:
#     def pdisplay(self):
#         print("This is parent property")

# class Child(Parent):
#     def cdisplay(self):
#         print("This is child property")

#Multi level inheritence
class GrandParent:
    def gpdisplay(self):
        print("This GP Display")
class Parent(GrandParent):
    def pdisplay(self):
        print("This is parent property")

class Child(Parent):
    def cdisplay(self):
        print("This is child property")

c = Child()
c.cdisplay()
c.pdisplay()
c.gpdisplay()