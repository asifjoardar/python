class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
class Supcal(Calculator):
    def sqr(self,a):
        return a*a
    def cube(self,a):
        return a*a*a
cal=Supcal()

print(cal.add(1,3))
print(cal.sub(3,1))
print(cal.mul(2,3))
print(cal.div(4,2))
print(cal.div(2,0))
print(cal.sqr(3))
print(cal.cube(3))
