"""
data = [{
    "id": 97407,
    "firstname": "Peter",
    "lastname": "Parker"
}, {
    "id": 97408,
    "firstname": "Khairi",
    "lastname": "Abu Bakar"
}, {
    "id": 97409,
    "firstname": "Aidawaty",
    "lastname": "Abdullah"
}]

def getFirstName(id):
    for student in data:
        if (student["id"] == id):
            return student["firstname"]

def getLastName(id):
    for student in data:
        if (student["id"] == id):
            return student["lastname"]
        
print("First Name:", getFirstName(97408))
print("Last Name:", getLastName(97408))
"""
