
a='bangladesh'
print(a[0])
print(a[0:9])
print(a[:2])
print(a[2:])
print(a[-1])


a='asif bgf'
a=a.capitalize()
print(a)
a=a.upper()
print(a)
b='i love bangladesh'
b=b.title()
print(b)
#a=a.lower()
a=a.casefold()
print(a)
c='JoArDaR'
c=c.swapcase()
print(c)
print(len(a))
a='asif'
b='joardar'
print(a+'-'+b) #asif-joardar
print('-'.join((a,b))) #asif-joardar
print(b.count('a')) #how many 'a' in b
print(b.count('a',3)) #how many 'a' in b after 3rd index
print(b.count('a',0,6)) #how many 'a' within 0-6 range of b
print(a.find('s'))
