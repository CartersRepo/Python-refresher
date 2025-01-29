def add(x, y):
    return x + y

print(add(5,7))

#re-write:
lambda x,y: x + y
#Here's also a valid way to give it a name: 
add = lambda x,y: x + y


#Use case: Makes the most sense to use map():
def double(x):
    return x*2

sequence = [1,3,5,9]
doubled = [x*2 for x in sequence]
#can be re-written like so:
doubled = [double(x) for x in sequence]

#And then further re-written:
doubled = map(double, sequence)

#Finally, achieving a lambda function with map:
doubled_final = map(lambda x: x * 2, sequence)

print(list(doubled_final))

