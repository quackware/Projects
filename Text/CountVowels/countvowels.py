#Count Vowels - Enter a string and the program counts the number of vowels in the text.
#For added complexity have it report a sum of each vowel found.

from collections import defaultdict

def main():
    inputString = input("Enter a string to count vowels or Exit.\n")
    vowelDict = defaultdict(int)
    vowels = ["a","e","i","o","u"]
    while inputString != "Exit":
        for c in inputString:
            if c.lower() in vowels:
                vowelDict[c.lower()] += 1
        
        for key in sorted(vowelDict.keys()):
            print (key, vowelDict[key])
        
        inputString = input("Enter a string to count vowels or Exit.\n")

if __name__ == '__main__':
    main()