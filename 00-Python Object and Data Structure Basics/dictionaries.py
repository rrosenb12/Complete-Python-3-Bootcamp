# Dictionaries
## Unordered mappings for storing objects using key-value pairings
### Can't be sorted
### Don't need to know an index location to find an object
## Uses curly braces {} and colons : to sifnify the relationship and commas to separate

my_dictionary = {'key1':'value1','key2':'value2'}
my_dictionary['key1']
# 'value1'

price_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}
price_lookup['apple']
# 2.99

# Can hold lists or other dictionaries
mixed_dictionary = {'integer':123,'list':[1,2,3],'dictionary':{'inside_dictionary':'inside_value'}}
mixed_dictionary['dictionary']['inside_dictionary']
mixed_dictionary['list'][2]

# Can add key:value pairs
mixed_dictionary['new pair'] = 'new value'

# .keys() will return all the keys
# .values() will return all the values
# .items() will return all the key:value pairs
print(mixed_dictionary.keys())
# dict_keys(['integer', 'list', 'dictionary', 'new pair'])
print(mixed_dictionary.values())
# dict_values([123, [1, 2, 3], {'inside_dictionary': 'inside_value'}, 'new value'])
print(mixed_dictionary.items())
# dict_items([('integer', 123), ('list', [1, 2, 3]), ('dictionary', {'inside_dictionary': 'inside_value'}), ('new pair', 'new value')])