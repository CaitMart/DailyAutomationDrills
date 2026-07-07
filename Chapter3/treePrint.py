def userInput(): 
    size = int(input("Enter the size of the tree "))
    tree(size)

def tree(size):

    for i in range(1, size+1):
        print("-")
        for i in range(size-i):
            print("^")
        else: print("-")
        



def main(): 
    userInput()

main()