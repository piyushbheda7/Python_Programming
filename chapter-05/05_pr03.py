# Can we have a set with 18(int) and “18”(str) as a value in it?

# s = { 18 , '18 } -> we can also define like this
s = set()

s.add(18)
s.add('18')

print(s)

print("Yes we have a set with 18 as integer and 18 as a string")