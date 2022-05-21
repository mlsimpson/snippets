import random

class SecretNumber:

    def __init__(self, num=None):
        if num:
            self.num = num
        else:
            # randomizing max range prevents known range
            # mitigates "just binary search b/w 1 and max"
            rand_max = random.randrange(999, 999_999_999_999)
            self.num = random.randrange(1, rand_max)

    def greater_than(self, guess):
        if self.num > guess:
            return True

        return False

    def less_than(self, guess):
        if self.num < guess:
            return True

        return False

    def equals(self, guess):
        if guess == self.num:
            return True

        return False

    def print_num(self):
        print(self.num)


# Using SecretNumber class + functions, guess number
# start at 1, increase by powers of 2
# each guess, record "previous guess"
# when less_than == True, perform binary search between
# previous guess and current guess

n = SecretNumber()

prev_guess = 1
curr_guess = 1

answer = None
answered = False

# n.print_num()

while not answered:
    if n.less_than(curr_guess):
        # perform binary search
        top = curr_guess
        bottom = prev_guess

        while not n.equals(answer):
            mid = (top + bottom) // 2
            answer = mid

            if n.less_than(mid):
                top = mid
            else:
                bottom = mid
        answered = True
    else:
        # increase guess by curr_guess * 2
        prev_guess = curr_guess
        curr_guess = curr_guess * 2

print(answer)

