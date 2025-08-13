print(hash("apple"))     
print(hash(12345))     


# dict uses hash to store/retrieve keys
person = {
    "name": "Alice",
    "age": 25,
}

print("name" in person)   # True (fast O(1) avg)
print("dateOfBirth" in person)
print(person['name'])

