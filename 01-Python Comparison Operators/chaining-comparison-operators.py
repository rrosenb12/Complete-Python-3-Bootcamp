2 < 3
# True
1 < 2
# True

# Another way to use 'and'
1 < 2 and 2 < 3
# True
1 < 2 < 3
# True
1 < 2 > 3
# False

# 'or'
1 == 1 or 2 == 2
# True
1 == 2 or 2 == 2
# True
1 == 2 or 2 == 1
# False

# 'not'
1 == 1
# True
not(1 == 1)
# False
not 1 == 1
# False