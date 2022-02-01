# set of 3 natural numbers where (a < b < c)
# a^2 + b^2 = c^2
#
# find one where a + b + c == 1000

def pythagoreanTriplet():
    max = 500

    for a in range(max, 1, -1):
        for b in range(max, a + 1, -1):
            # for c in range(b + 1, max):
            c = 1000 - (a + b)
            if (a**2 + b**2) == c**2:
                # if (a + b + c) == 1000:
                return "a", a, "b", b, "c", c


print(pythagoreanTriplet())

