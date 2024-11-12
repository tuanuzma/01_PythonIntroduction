# Take age as input
# age less than 10 is children
# age greater than equals to 10 and less than 18 is minor
# age greater than or equals to 18 and less than 21 is Teenager
# age greater than or equals to 21 and less than 60 is Adult
# age greater than or equals to 60 and above is Senior


age = int(input("What is your age: "))

if (age < 10):
    print("age", age, "I am a Children")
elif (age >= 10 and age < 18):
    print("age", age, "I am a Minor")
elif age >= 18 and age < 21:
    print("age", age, "I am a Teenager")
elif age >= 21 and age < 60:
    print("age", age, "I am a Adult")
else :
    print("age", age, "I am a Senior")
    

MR. JEGAN ANSWER====================================================

# Take age as input
# age less than 10 is children
# age greater than or equals to 10 and less than 18 is minor
# age greater than or equals to 18 and less than 21 is Tenager
# age greater than or equals to 21 and less than 60 is Adult
# age greater than or equals to 60 and above is Senior
age = int(input("Enter age: "))
if (age < 10):
    print("Children")
elif (age >= 10 and age < 18):
    print("Minor")
elif (age >= 18 and age < 21):
    print("Tenager")
elif (age >= 21 and age < 60):
    print("Adult")
# elif (age >= 60):
#     print("Senior")
else:
    print("Senior")

print("Children") if (age < 10) \
    else print("Minor") if (age >= 10 and age < 18) \
    else print ("Tenager") if (age >= 18 and age < 21) \
    else print ("Adult") if (age >= 21 and age < 60) \
    else print("Senior")


   
    
