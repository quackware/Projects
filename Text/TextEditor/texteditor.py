import sys,getopt
import curses

def main(argv):
    
    inputFile = ''
    try:
        opts,args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        printUsage()
    for opt,arg in opts:
        if opt == 'h':
            printUsage()
        elif opt in ["-i","ifile="]:
            inputFile = arg
    
    if inputFile == '':
        inputFile = input("Please enter input file name:")
    
    
    stdscr = setupCurses()
    
    pad = curses.newpad(100,100)
    
    while 1:
        c  = stdscr.getch()
    

def setupCurses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.keypad(1)
    return stdscr

def terminate(stdscr):
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()

def printUsage():
    print("texteditor.py -i <file>")
    
if __name__ == '__main__':
    main(sys.argv[1:])