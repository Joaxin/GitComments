import cmath
import re


def quadratic():
    while True:
        try:
            L = re.sub(r'[^0-9\.-]', ' ', input('Enter three coefficients a,b,c: ').strip())
            # re.sub returns str
            a, b, c = [float(i) for i in L.split()]

            if a == 0:
                print("the equation is linear, not quadratic")
            else:
                # str.split returns a list
                d = (b**2) - (4 * a * c)
                sol1 = (-b - cmath.sqrt(d)) / (2 * a)
                sol2 = (-b + cmath.sqrt(d)) / (2 * a)
        except(TypeError, ValueError):
            print("You need 3 numbers, e.g '2 5 1'")
            return quadratic()
        except:
            print("Unknown occurred")
            return
        return print('{0}\n{1}'.format(sol1, sol2))
        ch=input("Please input \'c \' to end or any keys to continue \n")
        if ch !='c' and ch !='C':
            pass
        else:
            break
quadratic()
