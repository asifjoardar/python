def a(s):
    print("my name is ",s)
def b(x,y):
    return x+y
def c(a,b,c=3):
    return a+b+c
def d(*arr):
    for i in arr:
        print(i,end=" ")
    print("")
def e(**arr):
    print(arr)

a('asif')

print(b(1,2))

print(c(1,2))
print(c(1,2,5))

d(1,2,3,4,5)

e(x=1,y=2,z=3)
