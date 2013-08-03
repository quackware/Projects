'''
Check if Palindrome - Checks if the string entered by the user is a palindrome. 
That is that it reads the same forwards as backwards like "racecar"
We are folling spaces and punctuation correctly.
'''


def main():
    inputString = input("Enter a string to check if palindrome or Exit.\n")
    while inputString != "Exit":
        palindrome = True
        for index in range(len(inputString)):
            if inputString[index] != inputString[len(inputString) - index - 1]:
                palindrome = False
                break
        if palindrome:
            print("String " + inputString + " is a palindrome")
        else:
            print("String " + inputString + " is not a palindrome")
        
        inputString = input("Enter a string to check if palindrome or Exit.\n")

if __name__ == '__main__':
    main()