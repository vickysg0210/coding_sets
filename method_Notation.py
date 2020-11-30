class A(object):
    def m1(self, n):
        print(self)
    
    @classmethod
    def m2(cls,n):
        print(cls)

    @staticmethod
    def m3(n):
        pass


a = A()
a.m1(1)
A.m2(1)
A.m3(1)