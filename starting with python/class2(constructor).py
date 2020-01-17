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

cal=Calculator(45,3)

print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.div())
