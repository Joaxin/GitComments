import os
import time


def main():
    str = 'Welcome to 1000 Phone Chengdu Campus      '
    while True:
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0:1]
        # for Linux use os.system('clear') instead
        os.system('cls')


if __name__ == '__main__':
    main()
