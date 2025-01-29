name = "Bob"
greeting = "Hello, Bob"
fgreeting = f"Hello, {name}"

print(greeting)

name = "Carter"

print(greeting)
print(fgreeting)
print(f"Hello, {name}")


greeting2 = "Hello, {}"
#str.format
with_name = greeting2.format(name)

print(with_name)

multi_phrase = "Hello, {}. Today is {}."
formatted = multi_phrase.format("Carter", "Wednesday")
print(formatted)