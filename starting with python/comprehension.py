my=[i**2 for i in range(20) if i%2==0]
print(my)
my=['mohammad','ashrafuddowla','asif','joardar']
my={i for i in my if len(i)>4}
print(my)
a=['name','country']
b=['asif','bangladesh']
my={i:j for i,j in zip(a,b)}
print(my)
