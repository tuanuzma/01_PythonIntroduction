# DATA STRUCTURE : SET

# Set uses {} = curley bracket
# set is not indexed
# set is not ordered
# set using for loop to pull out item in iterable object not using indexed
# example : set is like a bag which is full of items. when we want to take out a thing. 
# so we just tunggengkan beg terbalik dan keluarkan semua
# not ordered in set means not sorting
fruits = {"apple", "orange", "mango", "banana", "durian"}
print(fruits)

# print(fruits[0]) # cannot use index not subscriptable

# however it is iterable
for fruit in fruits:
    print(fruit)

# More than one item assigned to a single variable is called "Iterable Object"
# Not all Iterable objects are "Subscriptable"

# set does not allow duplicates
fruits = ["apple", "orange", "mango", "banana", "apple", "grapes", "apple", "durian"]
print(fruits)
# you can always typecast any iterable object to a set using set function
fruitsset = set(fruits)
print(fruitsset)

# We cannot append (adding as last item) an item, since is is not indexed
# However we can add an new item to the existing set
fruitsset.add("rambutan")
print(fruitsset)

# Can i remove an existing item
fruitsset.remove("apple")
print(fruitsset)

# You can also remove an item randomly using pop method
# ofcourse not popular
fruitsset.pop()
print(fruitsset)

# you can clear all the items inside the set
fruitsset.clear()
print(fruitsset) # the empty set is printed as "set()" because {} is also used by dictionary

# what if I want to add more than one from to the set
fruitsset = {"apple", "orange", "mango", "banana", "grapes"}
localfruits = {"cempedak", "mangosteen", "grapes", "durian", "rambutan"}
fruitsset.update(localfruits)
print(fruitsset)

print("=" * 80)

# SET ARITHMETIC
localfruits = {"cempedak", "mangosteen", "banana", "durian", "rambutan"}
overseafruits = {"apple", "orange", "mango", "grapes", "banana"}

# Let us get all the fruits
allfruits = localfruits.union(overseafruits)
print(allfruits)
# Let us get fruits which are available locally and in oversea
commonfruits = localfruits.intersection(overseafruits)
print(commonfruits)
# Let us get fruits which are available only in Malaysia
malaysianfruits = localfruits.difference(overseafruits)
print(malaysianfruits)
# Let us get fruits which are totally not in Malaysia
importedfruits = overseafruits.difference(localfruits)
print(importedfruits)

favoritefruits = {"durian", "rambutan", "mangosteen"}
# whether all my favorite fruits are available locally
print(favoritefruits.issubset(localfruits))
# whether locally available fruits are superset of my favorite fruits
print(localfruits.issuperset(favoritefruits))

# that means my favorite fruits is totally disjoint with oversea fruits
print(favoritefruits.isdisjoint(overseafruits))

# Get me all the fruits but minus the fruit which is available in both places
print(localfruits.symmetric_difference(overseafruits))

# find the result and update the localfruits with result (then use update)
# careful you going to loose the data in localfruits
localfruits.intersection_update(overseafruits)
print(localfruits)

# set is a function that help us to create set object
# similarly frozenset is another built in function that help us to create readonly set object
# this is similar to list (modifiable) and tuple (read only list)
# this is similar to set (modifiable) and frozenset (read only set)
readonlyset = frozenset({"apple", "orange", "mango", "banana"})
print(readonlyset)
