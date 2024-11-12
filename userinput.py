def keyboardInput(caption, datatype, errormessage):
    value = None
    isErrorInput = True
    while (isErrorInput):
        try:
            value = input(caption)
            value = datatype(value)
        except:
            print(errormessage)
        else:
            isErrorInput = False
    return value

# this code will get executed only if you type "python userinput.py" in the terminal
# this code will not get executed if you run "python functionspartone.py" in the terminal
if __name__== '__main__':
    principle = keyboardInput("Principle Amount: ", int, "Principle Amount must be Integer")
    period = keyboardInput("Period in Years: ", int, "Period must be Integer")
    rate = keyboardInput ("Rate in Percentage: ", float, "Rate must be float")
    interest = (principle * period * rate) / 100
    print("Interest Amount: ", interest)



