#return value is none by default.
def hello():
    print("Hello.")

def add(x, y=19):
    return x + y

print(add(5, 7))
print(add(5))
