# Similar to lists, but:
## Are immutable
### Once an element is inside a tuple, it can't be reassigned
## Use paranthesis instead of brackets

t = (1,2,3)
mylist = [1,2,3]

type(t)
# tuple

type(mylist)
# list

len(t)
# 3

# Can used mixed object types

t = ('one',2)
t[0]
# 'one'
t[-1]
# 2

t = ('a','a','b')
t.count('a')
# 2

t.index('a')
# 0
# Returns first time it appears