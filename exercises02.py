# Find the biggest digit in 78693

givennumber = 78693
temporarynumber = 0
result = 0

tempnumber = givennumber % 10
if result < tempnumber : result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber : result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber : result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber : result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber : result = tempnumber
givennumber = givennumber // 10
print(givennumber)
print(result)


# OR

# Find the biggest digit in the given number 78693
givennumber = 78693
tempnumber = 0
result = 0
tempnumber = givennumber % 10
if result < tempnumber: result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber: result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber: result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber: result = tempnumber
givennumber = givennumber // 10
tempnumber = givennumber % 10
if result < tempnumber: result = tempnumber
givennumber = givennumber // 10
print(givennumber)
print(result)
