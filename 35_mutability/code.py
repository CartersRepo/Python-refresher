a = []
b = a

print(id(a))
print(id(b))

a = ()
b = ()

#Everything is mutable except for: tuples, integers, floats, strings and booleans