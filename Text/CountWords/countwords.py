'''
Count Words in a String - Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a summary.
Modified it to count unique words.
'''

from collections import defaultdict


def main():
    f = open("in.txt","r")
    my_dict = defaultdict(int)
    count = 0
    for line in f:
        words = line.split()
        for word in words:
            if my_dict[word] != 1:
                count += 1
                my_dict[word] = 1
    print(count)

if __name__ == '__main__':
    main()