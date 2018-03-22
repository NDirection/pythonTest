class A(object):
    va = 10

    def foo(self):
        print( A.va)
        print (self.va)


        print("$$$$$$$$$$$$$$$$")

        self.va = 40
        print (A.va)
        print (self.va)

        print("$$$$$$$$$$$$$$$$")

        va = 20
        print (va)
        print(A.va)
        print(self.va)

        print("$$$$$$$$$$$$$$$$")
        A.va = 15
        print (A.va)
        print (self.va)
        print("$$$$$$$$$$$$$$$$")

# Script starts from here

obj1 = A()
obj2 = A()
obj1.foo()
print (A.va)
print (obj1.va)
print (obj2.va)