
a  = [10,70,90, 250]
y = bytes(a)
print(y)
print(type(y))
#bytes data type elements using index
b = [10, 30, 50 ,60 ,70 ,100, 120, 200]
y=bytes(b)
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
print(y[5])
print(y[6])
print(y[7])
print(y)
print(type(y))
#using for loop
# x =[10,20,30,40,50,60]
# y = bytes(x)
# for a in x:
#     print(a)
#values must be in range of  0 to 256
# c = [10, 350, 60, 70,90]
# d = bytes(c)
# print(d)
# print(dir(bytes))
#immutable
e = [10,20,30,40]
f = bytes(e)
y[0] = 20