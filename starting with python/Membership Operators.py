#Membership Operators ( in, not in )

a='Md Asif Joardar'
b='Asif'
if((b in a) == True):
    print('wow\n')
else:
    print('hush\n')

a=[1,2,3,4,5]
x=5
if((x not in a)):
    print('%d is not present in list\n'%x)
else:
    print('%d is present in list\n'%x)
