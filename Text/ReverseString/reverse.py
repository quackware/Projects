
def main():
    input = raw_input("Enter a string to reverse or Exit.\n")
    while input != "Exit":
        reverse = input[::-1]
        print("Reverse: " + reverse)
        input = raw_input("Enter a string to reverse or Exit.\n")

if __name__ == "__main__":
    main()