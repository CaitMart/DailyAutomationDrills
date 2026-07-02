#write a program that accepts the length and width of a rectangle from the user and then calculate both the perimeter and area of the space. 

#calculates the perimeter of the rectangle 
def perimeter(length, width):
    return 2 * (length + width)
#calculates the area of the rectangle
def area(length, width):
    return length * width

def userInput():
    width = int(input("Enter the width of the rectangle: "))
    length = int(input("Enter the length of the rectangle: "))
    print("\nResults")
    print("the area of the rectangle: ", area(length, width))
    print("the perimeter of the rectangle: ", perimeter(length, width))

def main():
    userInput()

main()