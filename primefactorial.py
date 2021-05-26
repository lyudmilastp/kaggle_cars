import functools

def prime(n):
    if n > 1:
        if n <= 3:
            return True
        for i in range(2,int(n ** 0.5 + 1)):
            if n % i == 0:
                return False
        return True

def find_even(n):
    num = 0
    for i in str(n):
        if int(i) in [2,4,6,8,0]:
            num = num + 1
        pass
    return num

@functools.lru_cache(1000)
def f(n):
    ans = [(find_even(i), i) for i in range(n) if prime(i)]
    return sorted(ans)[-1][1]

f(10000)