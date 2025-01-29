#Can modify a list
l = ["Bob", "Carter", "Annie"]

#Can't modify tuple
t = ("Bob", "Carter", "Annie")

#Order is not guaranteed when printing out, all unique values.
s = {"Bob", "Carter", "Annie"}

l.append("Smith")

print(l)

l.remove("Bob")

print(l)

s.add("Smith")
s.add("Smith")

print(s)