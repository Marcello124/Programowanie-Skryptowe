from math import sqrt
from sys import argv

def is_prime(number):

    if number == 0 or number == 1:
        return False

    for divisor in range(2, int(sqrt(number) + 1)):
        if not number % divisor:
            return False

    return True

if __name__ == "__main__":
    
    numbers = [int(i) for i in argv[1:] if i.isdigit()]

    for number in numbers:
        if is_prime(number):
            print(number)
