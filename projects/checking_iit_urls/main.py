# importing libraries
import requests
import sys
import scraping
import time


def main():
    # checking how user want to add the url
    print("To add the urls via a file type 'f'\nTo add a single url to type 't'\nTo add a key word type 'k'\nTo end the program type 'q'")
    choice = input("Enter the choice: ").lower()
    
    # clearing the files
    f1 = open("working.txt", "w")
    f2 = open("not_working.txt", "w")
    
    # checking the choice 
    if choice == "f":
        print("Enter the file name as a txt file")
        file_name = input()
        files(file_name)
    elif choice == "t":
        print("Enter the url coppied from the browser")
        url = input()
        urlopen(url)
    elif choice == "k":
        print("Enter the keyword to search for")
        keyword = input()
        google_search(keyword)
    elif choice == "q":
        sys.exit("Ending the program.")
    else:
        sys.exit("Invalid choice")
        
        
def files(name):
    print("Running.....", end="")
    f = open(name, "r")
    for line in f:
        print(line)
        check = requests.get(line)
        if check.status_code == 200:
            with open("working.txt", "a") as correct:
                correct.write(f"{line}\n")
        else:
            with open("not_working.txt", "a") as incorrect:
                incorrect.write(f"{line}\n")
    print("compelted.")
    
def urlopen(urlname):
    check = requests.get(urlname)
    if check.status_code == 200:
        print("This is working url")
    else:
        print("This is not working url")
    
    
def google_search(word):
    print("Running search...")
    urls = scraping.scraping(word)
    time.sleep(1)
    print("Urls are found")
    for url in urls:
        check = requests.get(url)
        if check.status_code == 200:
            print(f"\033[1;32m WORKS", end="")
            with open("working.txt", "a") as correct:
                correct.write(f"{url}\n")
        else:
            print(f"\033[1;31m BLOCK", end="")
            with open("not_working.txt", "a") as incorrect:
                incorrect.write(f"{url}\n")
        print(f"\033[1;34m \t{url}")
    print()
    print("\033[32m Completed.")
    
    
if __name__ == "__main__":
    main()