numbers = [12, 56, 98, 78, 56, 12, 26, 98]
person1 = ['Jamshed', 'Cox\'s Bazar', 23, 'Student']

# Key value pair
# Dictionary
# Object
# Hash table
# overlap with set
# That is mutable

# {key : value, key : value, key : value, ...}
person = {'Name' : 'Jamshed', 'Address' : 'Cox\'s Bazar', 'Age' : 23, 'Job' : 'Nope'}
print(person)
print(person['Name'])
print(person['Job'])
print(person.keys())
print(person.values())
person['Language'] = 'Python'
person['Name'] = 'Mumir'
del person['Age']
print(person)

# Special dictionary looping
for key, value in person.items():
    print(key, value)