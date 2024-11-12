# HOW TO MANIPULATE STRINGS DATA TYPE IN VARIABLES. 
# ONLY HAPPEN DURING PRE-PROCESSING NOT OUTSIDE SUCH AS WHEN PRINT FINAL OUTPUT!
# String literals are enclosed with double quote or
# single quote
message = "Hello World"
message = 'Hello World'
# In python actually no difference
# Here message is a string object
# which means message object will have many methods
# for example upper method will convert all characters to capital letter
print(message.upper()) # however this is not inline
# inline means do the changes and assign the changed value to the same variable
print(message)
# it is your responsible to capture the uppervalue into a variable and print it
## if we want to print it separately, we can create a new variable;
uppermessage = message.upper()
print(uppermessage)

print(message.lower())
print(message.capitalize())

## TRADITIONAL WAY
print("JCG" + str(8949))

carplate = "JCG"
number = 8949
carplatenumber = f"{carplate}{number}"
print(carplatenumber)

# ESCAPE SEQUENCE
# \n new line
# \t tab key
# \r carriage return
filepath = "c:\newfolder\table\report.txt"
print(filepath)
filepath = "c:\\newfolder\\table\\report.txt"
print(filepath)
# raw string
filepath = r"c:\newfolder\table\report.txt"
print(filepath)

# MULTILINE STRINGS
# it can be created using 3 double quote or 3 single quote
mystring = """While working on a data science project, we frequently 
encounter datasets that contain textual data in the form of strings. 
These strings often hold valuable information and their true potential 
can be realised by effectively manipulating and extracting insights 
from them. String manipulation techniques play a crucial role in 
data preprocessing, feature engineering, text mining, and 
natural language processing (NLP) tasks."""

# paragraph can be converted into list of words
# will split the sentences by space character
words = mystring.split()
print(words)
print(len(words))

# how to remove all the spaces in the string
# find the space and replace it with no space 
print(mystring.replace(" ", ""))
print(mystring.replace("A", "aaaaaaa"))

print(mystring.count("ing"))

# Index of the arguments. Can reuse it
# 0,1,2 is position of values
print("=" * 50)
mystring = "I bought {0:5d} {1:20s} for RM{2:10.2f}"
print(mystring.format(10, "Television", 1455.55))
print(mystring.format(11, "Radio", 657.25))
print("=" * 50)

# CONVERT LIST OF WORDS JOINING TOGETHER BECOME A STRING
# In the " " you can put any symbol you want.
print(words)
print("____".join(words))

# STRIP CAN REMOVE SPACE BETWEEN CHARACTER
mystring = "\nHello welcome to Python \n\t"
print(mystring.strip(), "123", sep="") # strip has remove space and \n " \n"
# We can safely say strip removes all the escape sequences
# at the beginning and end of the string
# and also the spaces at the beginning and end of the string
print(mystring.strip())
