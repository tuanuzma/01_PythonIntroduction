# DATA STRUCTURE (DICTIONARY)

# dictionary uses {}
# dictionary is indexed (using keys)
# dictionary is ordered
# dictionary is also referred as key-value pair
# In dictionary key must be unique, value can be duplicated

# Let us create a student data 
# student name is khairi (variable)
khairi = {
    "firstname": "Khairi",
    "lastname": "Abu Bakar",
    "icnumber": 720102121234,
    "subjects": ["BM", "BI", "Maths", "Science", "Social Science"],
    "active": True,
    "paid": True,
    "addresses": [
        {
            "street": "Jalan 26/1A",
            "area": "Cheras",
            "state": "Selangor",
            "country": "Malaysia"
        },
        {
            "street": "Lorog 101/103A",
            "area": "Petaling Jaya",
            "state": "Kuala Lumpur"
        }
    ]
}

# mynumbers = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# print(mynumbers[0][2])
print("First Name:", khairi["firstname"])
print("Last Name:", khairi["lastname"])
print("IC Number:", khairi["icnumber"])
print("Subject:", khairi["subjects"])
print("Active:", khairi["active"])
print("Paid:", khairi["paid"])

print("Addresses")
for address in khairi["addresses"]:
    print(address["street"])
    print(address["area"])
    print(address["state"])
    if ("country" in address.keys()):
        print(address["country"])

print(khairi.keys())
print(khairi.values())

print(khairi.items()) # list of tuple where each tuple has key, value. # items() is a method in dictionary
for key, value in khairi.items():
    print(key, value) # printing all the values one by one, first name, last name.

# If you assign a value to a key which is not there then the item
# will get added automatically
khairi["car"] = {
    "brand": "Proton",
    "model": "Saga",
    "number": "ABC1234"
}

print(khairi)

# if you assign a value to a key which already exist then the item
# gets updated
khairi["icnumber"] = 780102121234
print(khairi)

# This is to add country to the second address
khairi['addresses'][1]["country"] = "Malaysia"
# This is to modify the street value of the second address
khairi['addresses'][1]["street"] = "Lorong 105/110A"
print(khairi)

# add 3rd address to the existing list of addresses
khairi['addresses'].append({
    "street": "Lorog 101/103A",
    "area": "Petaling Jaya",
    "state": "Kuala Lumpur"
})
print(khairi)

# you can delete an item by key
khairi.pop("car")
print(khairi)

# dict is a function that help us to create an empty dictionary
newdictionary = dict()
print(newdictionary)
