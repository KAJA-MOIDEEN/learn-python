# Python Data Types

# In Python, data types classify the kind of value a variable holds and determine the operations that can be performed on it. Each value in Python has a specific data type. Python’s built-in data types include:

# 1.Integers: Whole numbers, both positive and negative.
age = 5 #integer
temprature = -5 # negative integer
# 2.floating-point :Number with decimal  point
pi=3.14 # floting-point float
weight = 65.5  # floating-point float

# 3.String : A sequence of characters, like a word or a sentence. Strings are enclosed in single quotes
name = "kaja" # string
greeting = "Hellow, world"  # string

# 4.Boolean: A boolean value can be either True or False
is_admin = True # boolean
is_admin = False # boolean

# 5.List: Ordered and mutable collections, allowing duplicates.
fruits = ["apple","orange","banana"] # list string
numbers = [1,2,3,4,5,6] #  list integer
both = [1,2,"three","four",5,6] # list  mixed data type
duplicate = [1,2,2,1,3,3]  # list duplicate data type its alows duplicate data type witch is repeted in list

# Creating a list
fruits = ["apple", "banana", "cherry", "apple"]

# Accessing elements by index
first_fruit = fruits[0]  # Output: "apple"
second_fruit = fruits[1]  # Output: "banana"

# Lists allow duplicates
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'apple']

# Lists are mutable - you can modify elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'apple']

# Adding elements to the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'apple', 'orange']

# Removing an element from the list
fruits.remove("apple")  # removes the first occurrence of 'apple'
print(fruits)  # Output: ['blueberry', 'cherry', 'apple', 'orange']

# 6. Tuples : oraderd but inmmutable collections.
person = ("kaja",24,"Chennai","male")
# accessing tuple element by index
name = person[0]
age = person[1]
city = person[2]
print(city)  # output Chennai
print(person)  # output ('kaja', 24, 'Chennai')
# tuples are immutable 
# person[1] = 23  # output TypeError: 'tuple' object does not support item assignment

# however, you can change  the entire tuple at once
person = ("kaja",23,"Chennai") # output ('kaja', 23,

print(person)

# 7 dictionaries  : unordered and mutable collections of key-value pairs
person = {
    "name":"kaja", # name is key kaja is value.
    "age":24,
    "city":"Chennai",
    "gender":"male" }
# accessing values by their keys
print(person["name"])
print(person["age"])

# modifying a value
person["age"] = 23
print(person)  # output {'name': 'kaja', 'age': 23, 'city': 'Chennai'}

# Adding a New Key-Value 
person["country"]="India"
person["job"]="Full Stack Developer"
print(person)   # output {'name': 'kaja', 'age': 23, 'city': 'Chennai', 'gender': 'male', 'country': 'India', 'job': 'Full Stack Developer'}
del person["job"]
print(person)

# 8.Sets: Unordered collections of unique elements.
unique_number = {1,2,3,3,2,1}
print(unique_number)