#prints rectangle of capital O characters that has a given height of 5 and a width given by the user. 


#prints rectangle with the width given by the user and a height of 5
def print_rectangle(width):
    height = 5
    for i in range(height):
        print('O' * width)

#gets user input for the width of the rectangle and calls the print_rectangle function
def user_height():
    width = int(input("Enter the width of the rectangle: "))
    print_rectangle(width) 

def main():
    user_height()

main()