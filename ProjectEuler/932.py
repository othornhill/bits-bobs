import math
#Project Euler, question 932: 2025
n = 16
#There's no need to waste time building a range and paring it. We can
#find the largest square that's still an n digit number.
maxi = math.floor(10**(n*0.5))

def square(x):
    return x * x

posvals = list(range(1,(maxi)))
squares = list(map(square,posvals))
#Mental math, no 2025 numbers smaller than 81
del squares[0:8]
vals = []
#First solution was taking a minute to brute force, need to pare down
#possibilities somehow. 
for x in squares:
    xs = str(x)
    xl = len(xs)
    #You have n-1 possible combinations of substrings for n digit num?
    for y in range(1,xl):
        f = xs[0:y]
        s = xs[y:xl]
        if str(x) == str((int(f)+int(s))**2):
            if s[0] != '0':
                vals.append(x)
sumtot = sum(vals)
print ("Sum of all 2025 numbers of " + str(n) + " digits is: " + str(sumtot))