import sys
from time import sleep

def main():
    phone_number = sys.argv[1]
    for digit in phone_number:
        print(f"{digit}...")
        sleep(1)
    print("Hahahaha!")


if __name__ == "__main__":
    main()
