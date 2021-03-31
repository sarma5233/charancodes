#EmptyList
y = []
x = list()
print(y)
print(x)
#concatenation
x = ['a', 'hello', 56.2, 98.4]
y = ['g']
print(x+y)
#repeatingy = ['a', 'b', 'c', 'd', 'e', 'f']
x =list()
print(y)
print(x)
print(x * 6)
#slicing
print(x[1:-1])
#indexing
print(x[:-1])
#appending
print(x.append(["hello"]))
print(x)
#extend
x.extend(['e','d'])
print(x)
#insert
x.insert(1 , 'Nike')
print(x)
#pop
print(x.pop(0))
print(x.pop(2))
print(x)
#list-mutable
print(x)
m = x + ['efghrg']
print(m)
print(id(m))
print(x.append('efghrg'))
print(id(x))



