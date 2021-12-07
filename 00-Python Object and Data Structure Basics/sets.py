# Sets are unordered collections of unique elements
## There can only be one representative of the same object

myset = set()
# set()

myset.add(1)
myset
# {1}

myset.add(2)
myset
# {1,2}

myset.add(2)
myset
# {1,2}
## Doesn't throw an error, doesn't add the 2

mylist = [1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3]
set(mylist)
# {1,2,3}