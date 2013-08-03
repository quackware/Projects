
def main():
    inputString = input("Enter a string to reverse or Exit.\n")
    while input != "Exit":
        reverse = inputString[::-1]
        print("Reverse: " + reverse)
        inputString = input("Enter a string to reverse or Exit.\n")

if __name__ == "__main__":
    main()