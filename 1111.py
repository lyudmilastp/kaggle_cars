import timeit
def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def prev_prime(n):
    n = n - 1
    while not prime(n):
        n = n -1
    return n


def find_even(n):
    num = 0
    for i in str(n):
        if int(i) in [2,4,6,8,0]:
            num = num + 1
        pass
    return num


def f(n):
    dig = prev_prime(n)
    while find_even(dig) < (len(str(n)) - 1):
        dig = prev_prime(dig)
    return dig


timeit.timeit('f(5000000)', globals = globals(), number = 1)
f(500)