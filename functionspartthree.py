# RECURSIVE FUNCTION

# recursive function is function calling the same function repeatedly.
# Let us find factorial of a given number
# fac(5) = 5 * 4 * 3 * 2 * 1
givenNumber = 5
factorial = 1
for currentNumber in range(givenNumber, 0, -1):
    factorial = factorial * currentNumber
print("Factorial of", givenNumber, "is", factorial)
# mathematically how to write the factorial(n)
# n * (n - 1) * (n - 2) * (n - 3) * (n - 4)
# n * (n - 1) * (n - 2) .... (n - (n - 1))
# n * (n - 1)!
# 5 * 4!
# 97432
# 2 * 10000 + reverse(9743)
# 2 * 10000 + 3 * 1000 + reverse(974)
# You can also use another technique called recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Factorial of", givenNumber, "is", factorial(5))

# sum of digits
def sumofdigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumofdigits(n // 10)

givenNumber = 97409
print("Sum of digits for", givenNumber, "is", sumofdigits(givenNumber))
