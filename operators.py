# Arithmetic operators
# --------------------------------------------------------
x = 20
y = 10
print(x + y) # addition
print(x - y) # subtraction
print(x * y) # multiplication
print(x / y) # division (always returns float)
# 2 more operators
x = 7
y = 3
print("Quotient:", x // y) # always return integer
print("Remainder:", x % y) # always return integer
x = 2
y = 3
print(x ** y) # 2 to the power of 3

# decimals
# 4.2 ceil  => 5
# 4.9 floor => 4
# 4.2 round => 4
# 4.9 round => 5

# Assignment Operators
# --------------------------------------------------------
x = 10 # equals to
# you can assign multiple values to multiple variables
x, y, z = 10, 11, 12
# x, y, z = 10
print(x, y, z)

# steps
step = 0
step = step + 1
step = step + 1

# steps (long legs)
step = 0
step = step + 2
step = step + 2
# there is a high chance for this guy to miss the floor
# the first floor is at step 21

# Step down
step = 60
step = step - 1
step = step - 1

# you can also write the above as follows
step += 1 # step = step + 1
step += 2 # step = step + 2

step -= 1 # step = step - 1
step -= 2 # step = step - 2

step *= 1 # step = step * 1
step *= 2 # step = step * 2

step /= 1 # step = step / 1
step //= 1 # step = step // 1
step %= 1 # step = step % 1
step **= 1 # step = step ** 1

# Comparison Operators
# --------------------------------------------------------
# Comparison operators always return TRUE or FALSE
# Comparison operators help us to make decisions
x = 10
y = 15
z = 10
# Let us create comparisons that return TRUE
print(x < y) # less than
print(y > x) # greater than
print(x != y) # not equals to
print(x == z) # equals to
print(x <= y) # less than or equals to
print(x <= z) # less than or equals to
print(y >= x) # greater than or equals to

# Logical Operators
# and, or, not => keywords in python
# xor in python (^)
# Truth Table for and operator
# print((condition1) and (condition2))
# Condition 1             Condition 2             Result
# True                    True                    True
# True                    False                   False
# False                   True                    False
# False                   False                   False

x = 10
y = 5
z = 8
print((x > y) and (x > z)) # biggest number
print((y < x) and (y < z)) # smallest number

# Can we print 1, 0 instead of True, False
print(int(True))
print(int(False))

# Truth Table for or operator
# print((condition1) or (condition2))
# Condition 1             Condition 2             Result
# True                    True                    True
# True                    False                   True
# False                   True                    True
# False                   False                   False

x = 10
y = 5
z = 8
print((x > y) or (x > z))
print((x > y) or (y > z))
print((y > z) or (x > y))
print((x < y) or (x < z))

# Truth Table for xor operator
# print((condition1) ^ (condition2))
# Condition 1             Condition 2             Result
# True                    True                    False
# True                    False                   True
# False                   True                    True
# False                   False                   False

print((x > y) ^ (x > z))
print((x > y) ^ (y > z))
print((y > z) ^ (x > y))
print((x < y) ^ (x < z))

# we also call the not as Negation Operator
# Negation means change True to False and False to True
# not is not a function it is a keyword
print("5 > 3", not (5 > 3))
print("5 < 3", not (5 < 3))

# Special Operators
x = 101
y = 101
print(id(x))
print(id(y))

print(x == y) # the comparison is done at value level
print(x is y) # the comparison is done at address level
