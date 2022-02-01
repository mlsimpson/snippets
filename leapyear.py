# year is divisible by 4
# if a year is divisible by 100, then its not a leap year
# if year is divisible by 400, then it is a leap year
# 1896: leap
# 1900: not leap
# 2000: leap

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(isLeap(1896)) # -> leap
print(isLeap(1900)) # -> not leap
print(isLeap(2000)) # -> leap

