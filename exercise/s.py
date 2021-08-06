class super1():
    def __init__(self):
        print('super2')

class sub1(super1):
    def __init__(self):
        #super1.__init__(self)
        super().__init__() #これでも動く
        print('sub')

s = sub1()