#Identity operators (is , is not)

a=10
if( type(a) is int ):
    print("ok\n")
else:
    print("nope\n")

a=5.5
b=5.5

if(a is b):
    print("ok\n")
else:
    print("nope\n")

a='asif'
b=22

if(type(a) is not type(b)):
    print("ok\n")
else:
    print("nope\n")
