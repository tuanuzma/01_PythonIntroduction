# list is an iterator
mynumbers = [10, 20, 30, 40, 50]
# Iterator are objects that can be iterated through a for loop
for mynumber in mynumbers:
    print(mynumber)

def addfive(n):
    return n + 5

mynumbersplusfive = map(addfive, mynumbers)
# map is also an iterator object
for mynumber in mynumbersplusfive:
    print(mynumber)

# iterator objects which we already tried
# list, tuple, set, frozenset, dictionary
# range, enumerate, map, filter, zip
fruits = ["apple", "orange", "mango", "durian", "television"]
colors = ["red", "orange", "yellow", "deep yellow"]
taste = ["sweeter", "sour", "sweeter", "sweeter"]
combination = zip(fruits, colors, taste)
# zip is also an iterator object
# zip will return tuple of tuples
# each tuple has one item from every list and it is ordered
for item in combination:
    print(item)

# We can also iterate any iterator object using iter built in function
mynumberiter = iter(mynumbers) # this will return the iterator
print(next(mynumberiter))
print(next(mynumberiter))
print(next(mynumberiter))
print(next(mynumberiter))
print(next(mynumberiter))
# we want to know whether next will give us an item or throw error
# by pass None as second argument if the next returns None then we know
# there is no more item in the iterator
print(next(mynumberiter, None))

hasnext = True
mynumberiter = iter(mynumbers)
while(hasnext):
    item = next(mynumberiter, None)
    if (item == None):
        hasnext = False
    else:
        print(item)
# However the above implementation is not necessary
# if this is your case to iterate the iterator then just use for loop
def multiplesoffive():
    number = 0
    yield number
    number = number + 5
    yield number
    number = number + 5
    yield number
    number = number + 5
    yield number

for mynumber in multiplesoffive():
    print(mynumber)

myiterator = iter(multiplesoffive())
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))

# stream a new value everytime you call him
def multiplesofseven():
    number = 0
    yield number
    while(number < 700):
        number = number + 7
        yield number

for mynumber in multiplesofseven():
    print(mynumber)

