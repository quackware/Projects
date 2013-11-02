'''
Whois Search Tool - Enter an IP or host address and have it look it up 
through whois and return the results to you.
'''
import subprocess

def main():
    host = ''
    host = raw_input("Enter host or ip address: ")
    while host != 'exit':
        # Just use whois, we should probaby do something else later.
        r = subprocess.Popen(['whois',host], stdout = subprocess.PIPE)
        stdout = r.communicate()
        print(stdout)
        host = raw_input("Enter host or ip address: ")

if __name__ == "__main__":
    main()
