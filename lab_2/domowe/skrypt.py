import re


def string_check(str):
    numbers = ''.join(re.findall('\d', str))
    letters = ''.join(re.findall('\D', str))

    return (numbers, letters)


if __name__ == "__main__":
    
    while 1:
        string = input()

        if string[0].isdigit():
            print(f"  Liczba: {string_check(string)[0]}\n  Wyraz: {string_check(string)[1]}")
        
        else: 
            print(f"  Wyraz: {string_check(string)[1]}\n  Liczba: {string_check(string)[0]}")
