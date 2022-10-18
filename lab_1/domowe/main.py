import cmath
from fractions import Fraction

def sum(arg1, arg2):
   
    if isinstance(arg1, float) or isinstance(arg2, float):
        return float(arg1) + float(arg2)
    elif isinstance(arg1, int) and isinstance(arg2, int):
        return int(arg1) + int(arg2)
    elif isinstance(arg1, complex) or isinstance(arg2, complex):
        return complex(arg1) + complex(arg2)
    elif isinstance(arg1, Fraction) or isinstance(arg2, Fraction):
        return Fraction(arg1) + Fraction(arg2)
    else:
        return float(arg1) + float(arg2)
    

print(f"__name__ = {__name__}")

if __name__ == '__main__':
    print(sum(2, 3))
