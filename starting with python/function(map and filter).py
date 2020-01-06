#map
arr=[1,2,3,4,5]
def sq(x):
    return x*x
arr1=list(map(sq,arr))
print(arr1)

#filter
def evn(x):
    if x%2:
        return False
    else:
        return True
arr2=list(filter(evn,arr))
print(arr2)
