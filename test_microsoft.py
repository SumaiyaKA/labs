import sys

def main():
    answer = input("Hi, would you like to play? Y/N ").upper()

    if answer == "Y":
        print("Hi!") 
    else:
        print("goodbye!")
        sys.exit()

if __name__ == "__main__":
    main()