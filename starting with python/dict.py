a={} #a=dic()
print(a)
print(type(a))
a={'name':'asif','age':'22','phn':'01902838503'}
print(a)
print(a['name'])
a['name']='joardar'
print(a)
a['from']='dhaka'
print(a)
del a['from']
print(a)
a.clear()
print(a)
a=a.get('name','kisu nai')
print(a)
a={'name':'asif','age':'22','phn':'01902838503'}
a=a.get('name','kisu nai')
print(a)
print(type(a))
a={'name':'asif','age':'22','phn':'01902838503'}
print('name' in a)
print(a.items())
print(a.keys())
print(a.values())
