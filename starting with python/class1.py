class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

cal=Calculator()

print(cal.add(12,78))
print(cal.sub(50,23))
print(cal.mul(9,19))
print(cal.div(400,5))
print(cal.div(12,0))
