# A dictionary is an unorders, mutable collection of key-value pairs.
# A dictionary is defined by a set of curly brackets {}
# Each key-value pair is separated by a comma.

#syntax: {key: value, key1: value1}

#Here's the example

marks = {
    "John": 90,
    "Emma": 85,
    "harry": 25 
}
print (marks, type(marks)) #output is {'John': 90, 'Emma': 85, 'harry': 25} <class 'dict'>

#you can print dictionaries like tuple using marks[0]
# you print by giving names marks[john]
print(marks["John"]) #output is 90

# you can also print all keys and values using .items()
print(marks.items())
#output is dict_items([('John', 90), ('Emma', 85), ('harry', 25)])

#or you can print keys and values separetly
print (marks.keys())
#output is dict_keys(['John', 'Emma', 'harry'])
print (marks.values())
#output is dict_values([90, 85, 25])