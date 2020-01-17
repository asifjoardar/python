class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
class Supcal(Calculator):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def add(self):
        return self.a+self.b+self.c

cal=Supcal(3,2,1)

print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.div())
