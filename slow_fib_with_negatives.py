def fib(n):
    cache = {-2: -1, -1: 1, 0: 0, 1: 1, 2: 1}
    if n in cache:
        return cache[n]

    else:
        index = 0
        if n >= 0:
            while index <= n:
                next_fib = cache[index - 2] + cache[index - 1]
                cache[index] = next_fib
                index += 1
            print(cache[index - 1])
            # return cache[index - 1]
        else:
            while index >= n:
                # print(index, cache[index])
                next_fib = cache[index] - cache[index - 1]
                cache[index - 2] = next_fib
                index -= 1
            print(cache[index + 1])
            # return cache[index + 1]

