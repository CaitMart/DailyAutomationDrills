#rewrite code given to fix errors and ensure there is input valildation to decide if a given temperature is safe

def userInput(): 
    scale = str(input("Enter C or F to indicate Celsius or Fahrenheit: "))
    degrees = int(input("Enter the number of degrees: "))
    isSafe(scale, degrees)

def scaleInputCheck(scale):
    print(scale.lower())
    if (scale.lower() != "c" or scale.lower() != "f"):
        print("The scale you entered is not valid please try again")
        userInput() 
    return

def isSafe(scale, degrees):
    scale = scale.lower()
    if scale == "c":
        if degrees >= 16 and degrees <= 38:
            print("celcius is safe")
    elif scale == "f":
        if degrees >= 60.8 and degrees <= 100.4:
            print("Fahrenheit is safe")
    else:
        print("Dangerous")

def main(): 
    userInput()

main()