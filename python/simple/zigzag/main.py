import sys
import time


def main():
    
    indentation = True
    indents = 0
    
    try:
        while True:
            if indentation == True:
                print(" " * indents, end="")
                indents += 1
                if indents == 20:
                    indentation = False
                    indents -= 1
            else:
                print(" " * indents, end="")
                indents -= 1
                if indents == 0:
                    indentation = True
            
            #printing * marks
            print("*" * 10)
            time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()
        
    

if __name__ == '__main__':
    main()