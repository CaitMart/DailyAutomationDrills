#fill in the previous program so that it is a single condition 


def userInput(): 
    scale = str(input("Enter C or F to indicate Celsius or Fahrenheit: "))
    degrees = int(input("Enter the number of degrees: "))
    isSafe(scale, degrees)


def isSafe(scale, degrees):
    scale = scale.lower()
    if (scale == "c" and (degrees >= 16 and degrees <= 38)) or (scale == "f" and(degrees >= 60.8 and degrees <= 100.4)):
        print ("Safe")
    else:
        print("Dangerous")

def main(): 
    userInput()

main()