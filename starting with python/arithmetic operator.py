# Reads two numbers from input and typecasts them to int using
# map function
a,b=map(int,input().split())

print(a+b)
print(a-b)
print(a*b)
print('%.10f'%float(a/b))
print(a%b)
print(a**b) #a^b
print(a//b) #floor
