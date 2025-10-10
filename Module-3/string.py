name = 'Sakib\'s khan' # escape
name2 = "Sakib Khan"

# Multi line string
name3 = """
    Sakib Khan
    number One
"""

print(name)
# String is a sequence of characters
for ch in name2:
    print(ch)

print(name2[3])
print(name2[1:6])
print(name2[::-1])


# Mutable means changable
# Immutable means you can't change it
# name2[0] = 'R' # Not possible
print(name2)
if 'Khan' in name2:
    print('Exist')

print(name2.upper())