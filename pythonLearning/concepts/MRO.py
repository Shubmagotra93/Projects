class A:
    def sum(self):
        print("I am class A")

class B:
    def sum(self):
        print("I am class B")

class demo(B, A):
    def show(self):
        print("I am class DEMO")

c = demo()
c.show()
print(demo.mro())