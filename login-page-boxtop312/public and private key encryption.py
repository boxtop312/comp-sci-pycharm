import random

e = 64049653
p = 180406337
q = 385713907
N = q * p
T = (p - 1) * (q - 1)


def isprime(x):
    if x > 1:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        else:
            return True
    else:
        return False


def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


def primes_less_than(n):
    all_primes = []
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            all_primes.append(p)
    return all_primes


for d in primes_less_than(999999999):
    if (e*d) % T == 1:
        print(d)
        break
    else:
        print(d, 0)

