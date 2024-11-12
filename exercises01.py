# Reverse the given number 98765
# the expected output: 56789

input = 98765
output = 0

output = input % 10
input = input // 10
print(input)
print(output)

output = (output * 10) + (input % 10)
input = input // 10
print(input)
print(output)

output = (output * 10) + (input % 10)
input = input // 10
print(input)
print(output)

output = (output * 10) + (input % 10)
input = input // 10
print(input)
print(output)

output = (output * 10) + (input % 10)
input = input // 10
print(input)
print(output)

# OR

# Reverse the given number 98765
# the expected output: 56789
givennumber = 98765
result = 0
result = givennumber % 10
givennumber = givennumber // 10
result = result * 10 + (givennumber % 10)
givennumber = givennumber // 10
result = result * 10 + (givennumber % 10)
givennumber = givennumber // 10
result = result * 10 + (givennumber % 10)
givennumber = givennumber // 10
result = result * 10 + (givennumber % 10)
givennumber = givennumber // 10
print(givennumber)
print(result)
