sum=lambda a,b : a+b
print(sum(1,2))
print((lambda a,b:a+b)(10,20))

def a(f,x,y):
    return f(x,y)
print(a((lambda x,y:x+y),5,6))
