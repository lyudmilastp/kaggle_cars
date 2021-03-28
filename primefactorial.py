"2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"
import itertools
from functools import reduce
import math
import collections
from operator import mul

# Function to determine whether the number is prime

def prime(n):
    if n <= 3:
        return True
    else:
        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0:
                return False
        return True


# Function for decomposition "n"
def decomp(n):
    # n! value calculating
    n_fact = math.factorial(n)
    # all the parts of factorial sequence
    n_parts = [i for i in range(n, 2, -1)]
    ans = []

# If number is prime -> power = 1
    for i in n_parts:
        if prime(i):
            ans.append(i)
            n_parts.remove(i)


# Production of all numbers in the updated list
    new_num = reduce(mul, n_parts, 1)
# Divide number by 2 till it's divisible by 2. Otherwise a = 3, divide by 3... etc.
    a = 2
    while not prime(new_num):
        if new_num % a == 0:
            new_num = new_num / a
            ans.append(a)
        else:
            a += 1

# Counting the number of divisions of each number
    counts = collections.Counter(ans)

    return ' * '.join([(str(i)+'^'+str(counts[i])) for i in sorted(counts)])


