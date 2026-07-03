# avoid using the + or * operators to add or multiply their arguments 
# program should be adding 1 at a time to get the final result 

def userInput(): 
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    operator = str(input("Enter + to add or enter * to multiply: "))
    if operator == "+": add_number(number1, number2)
    elif operator == "*": multiply_number(number1, number2)

def plus_one(number):
    total = (number + 1)
    return total


def add_number(number1, number2):
   total = number1
   for i in range(number2):
       total = plus_one(total)
   print('addition total: ', total)
   
def multiply_number(number1, number2):
    total = number1
    for i in range(number2):
        total = total + number1
    total -= number1
    print("multiplication total: ", total)

def main():
    userInput()


main()