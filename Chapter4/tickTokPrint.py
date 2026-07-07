import time 

def userInput(): 
    secondsPaused = int(input("How many seconds for pause?: "))
    ticktok(secondsPaused)


def ticktok(secondsPaused):
    tick = True 

    try:
        while True:
            if tick:
                print("tick ", flush=True)
            else: print("toc ", flush=True)
            tick = not tick
            time.sleep(secondsPaused-1)
    
    except: 
        if(secondsPaused == 0): exit


def main(): 
    userInput()

main()