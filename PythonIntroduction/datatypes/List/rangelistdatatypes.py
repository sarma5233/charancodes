a = range(10)
print(a)
for x in a:
    print(x)
    print(type(x))
    # print(dir(list))
    #Creations oflist
    b = list(range(1, 10))
    print(b)
    #Indexing
    b = list(range(1,10))
    print(a[0])
    print(a[3])
    print(a[9])
    #Out Of range
    b = list(range(1,20))
    print(a[30])
