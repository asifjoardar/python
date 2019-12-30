def bitmask(str):
    n = int(2**len(str))
    for i in range (1,n):
        for j in range(0,len(str)):
            if (i&(1<<j)):
                print(str[j],end="")
        print("")

str = str(input())
bitmask(str)
