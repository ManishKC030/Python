# Note: Python does not have built-in Arrays, but Lists can be used instead.
# You can achieve it using NumPy library.


###using Lists as Arrays

#you can use lists as an array, as list can store any data type
# to use Lists as array you should only use same datatypes

cars = ["BMW", "Honda", "Nissan", "Toyota"]
print(cars[0])  # BMW
print(cars[1])  # Honda
print(cars[3])  # toyota

#use len() to retuen length of array
print(len(cars))  # 4

#loop in array
for i in cars:
    print(i)
