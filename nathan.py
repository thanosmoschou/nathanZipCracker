"""
Author: Thanos Moschou
Date: 08/2023
Description: This is a simple zip cracker tool. It uses dictionary attack in order to crack the password of a locked zip file.
Disclaimer: This is a proof of concept and is made for educational purposes only. 
Never use this tool to crack any file without file owner's licence. 
Use it at your own risk. 
I am not responsible for any harm you may cause by using this tool. 
Also there are a lot of similar tools on the market, which are better and faster. 
I just implemented it because I wanted to learn how these tools work.
This tool is slow if you specify a big dictionary. 
"""

import zipfile
import time
import argparse

def crack(zipFileName, passwordListName):
    zipFile = zipfile.ZipFile(zipFileName)
    with open(passwordListName, 'rb') as filename:
        for passwd in filename:
            #Remove the \n of linux or \r\n of windows. 
            #Convert the password to string first (because you cannot make modifications in bytes format) and do the modification.
            passwd = passwd.decode(encoding = 'utf-8')
            pas = passwd[:-2] if passwd.endswith('\r\n') else (passwd[:-1] if passwd.endswith('\n') else passwd)
            pas = bytes(pas, encoding = 'utf-8') #convert to bytes again because extractall method needs password in bytes format 
            try:
                zipFile.extractall(pwd = pas)
                print(f"Password Found: {pas.decode(encoding = 'utf-8')}")
                return True
            except:
                print(f"Password tried: {pas.decode(encoding = 'utf-8')}")
        return False


def main():
    parser = argparse.ArgumentParser(description = "The wannabe zip cracking tool")

    #metavar is placed in help messages. It indicates that at this place an argument must be placed
    parser.add_argument("-f", "--file", metavar = 'File' , type = str, help = "Specify the password locked zip file you want to crack.", required = True)
    parser.add_argument("-l", "--list", metavar = 'List' , type = str, help = "Specify the dictionary you will use in this attack.", required = True)

    args = parser.parse_args()

    zipFileName = args.file #or args.f if you ONLY specify short flag. If you specify both short flag and long flag, the Namespace will have attributes specified by the long flag name
    passwordListName = args.list #or args.l for the same reason

    start = time.time()

    if crack(zipFileName, passwordListName) == False:
        print("Password not found...")

    end = time.time()

    print(f'Total time needed: {end - start} seconds.')


if __name__ == "__main__":
    main()