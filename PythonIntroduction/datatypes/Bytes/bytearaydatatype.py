a = [10,20,30,40]
b = bytearray(a)
print(b)
print(type(b))
#bytes data type elements using index
c = [20,30,40,50]
d = bytearray(c)
print(d[0])
print(d[1])
print(d[2])
print(d[3])
print(d)
print(type(d))
#Using for loop
e = [10,20,30,40]
f = bytearray(e)
for a in f:
    # print(f)
    print(a)
#using the values from  0 to 256
# g = [25,300,100,350]
# f = bytearray(g)
# print(f)
print(dir(bytearray))
#mutable
h = [10,20,30,40,50]
i = bytearray(h)
print("befor modyfing h[0]value:", h[0])
h[0] = 30
print("after modyfying the h[0] value :", h[0])
