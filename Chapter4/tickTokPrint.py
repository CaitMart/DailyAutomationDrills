import time 

def userInput(): 
    secondsPaused = int(input("How many seconds for pause?: "))
    ticktok(secondsPaused)

def ticktok(secondsPaused):
    tick = True
    while secondsPaused != 0:
        if tick:
            print("tick ", flush=True)
        else: 
            print("toc ", flush=True)
        tick = not tick
        time.sleep(secondsPaused)
        secondsPaused = secondsPaused - 1
   
def main(): 
    userInput()

main()
