import functools

@functools.lru_cache()
def fib_recursive(nth):
    if nth < 2:
        return nth
    else:
        return (fib_recursive(nth - 1)) + (fib_recursive(nth - 2))

def fib_iterative(nth):
    two_before = 0
    one_before = 1
    index = 0

    while(index < nth):
        new_one_before = two_before + one_before
        two_before, one_before = one_before, new_one_before
        index += 1

    return two_before

print(fib_recursive(100))
print(fib_iterative(100))

