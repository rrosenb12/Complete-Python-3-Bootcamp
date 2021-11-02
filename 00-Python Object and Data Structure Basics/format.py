# .format() method
## 'String here {} then also {}'.format('something1','something2')
### {} is string interpolation

print('This is a string {}'.format('idiot'))

print('The {2} {1} {0}'.format('fox','brown','quick'))
# Can use index positions in {}

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
# Can also use variables

# Can also format numbers

result = 100/777
print('The result was {r}'.format(r=result))
# The result was 0.1287001287001287

# Formatting a float number
## {value:width.precision f}
### value - in this case, r
### width - how many white spaces before the first digit
#### 1 will give you one space
### precision - which decimal point to go up to

print('The result was {r:10.3f}'.format(r=result))
# The result was      0.129