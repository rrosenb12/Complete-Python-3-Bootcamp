# Lists are ordered sequences that can hold a variety of object types
## Use square brackets [] and commas ,
### [1,2,3,4,5]
## Can be indexed and sliced
## Can be nested

my_list=[1,2,3]
my_list[0]
# 1

my_list[1:]
# Everything after and including index 1

# Can also be composed of mixed object types
my_mixed_list = ['STRING',100,23.2]

# Can concatenate lists
new_list = my_list + my_mixed_list
# [1,2,3,'STRING',100,23.2]

# Can change/edit elements in the list
new_list[0] = "One as a string"
print(new_list)
# ["One as a string",2,3,"STRING",100,23.2]

# .append() method
## adds onto the end of the list
new_list.append('six')
print(new_list)
# ["One as a string",2,3,"STRING",100,23.2,'six']

# .pop() method
## removes and returns last element in the list
new_list.pop()
# 'six'

# .pop() can also remove whatever index you specify
new_list.pop(2)
# 3

# .sort() method
my_letter_list = ["a","b","e","z","f"]
my_letter_list.sort()
print(my_letter_list)
# You have to call my_letter_list.sort() and then do print(my_letter_list) because .sort() occurs in place
## Calling print(my_letter_list.sort()) returns None
### If you call type(my_letter_list.sort()) you will get NoneType
#### None object
##### Return value of a function or method that doesn't return anything
### The same thing will happen if you assign the result to something else 
#### For example
##### `my_sorted_list = my_letter_list.sort()``
###### Will return None
#### You will have to assign after it is sorted

# .reverse() method
## Will reverse your list
## Also happens in place