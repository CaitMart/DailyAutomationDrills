#rewrite code given to fix errors to decide if a given temperature is safe

def userInput(): 
    scale = str(input("Enter C or F to indicate Celsius or Fahrenheit: "))
    degrees = int(input("Enter the number of degrees: "))
    isSafe(scale, degrees)


def isSafe(scale, degrees):
    scale = scale.lower()
    if scale == "c":
        if degrees >= 16 and degrees <= 38:
            print("celcius is safe")
        else:
            print("dangerous")
    elif scale == "f":
        if degrees >= 60.8 and degrees <= 100.4:
            print("Fahrenheit is safe")
        else:
            print("dangerous")
    else:
        print("Dangerous")

def main(): 
    userInput()

main()