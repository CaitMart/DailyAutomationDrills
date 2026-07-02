#write a program that accepts an int from the user. if it is divisible by 3  it prints fizz, 
#if it is divisible by 5 it prints buzz. If it it divisible by both it prints fizz buzz
#and if it is not divisible by either it will just print the value the user entered 


def userInput(): 
    userNumber = int(input("Enter an integer: "))
    fizzBuzz(userNumber)

def fizzBuzz(userNumber):
    if (userNumber % 3 == 0 and userNumber % 5 == 0): print("Fizz Buzz")
    elif userNumber % 3 == 0: print("Fizz")
    elif userNumber % 5 == 0: print("Buzz")
    else: print(userNumber)

def main(): 
    userInput()

main()