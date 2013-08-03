#Reverse a String - Enter a string and the program will reverse it and print it out.


def main():
    inputString = input("Enter a string to reverse or Exit.\n")
    while inputString != "Exit":
        reverse = inputString[::-1]
        print("Reverse: " + reverse)
        inputString = input("Enter a string to reverse or Exit.\n")

if __name__ == "__main__":
    main()