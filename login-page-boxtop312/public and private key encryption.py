import random

p = 47
q = 13
e = 421
d = 493


def calculate_N(p, q):
    return q * p


def calculate_T(p, q):
    return (p - 1) * (q - 1)


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


def pick_e_d(p, q):
    # (e*d)%T == 1
    # ((T+1)/e or d)  = e or d
    T = calculate_T(p, q)
    N = calculate_N(p, q)
    newlist = primes_less_than(T)
    d_list = []
    for e in newlist:
        if not is_coprime(e, T) and not is_coprime(e, N) and e < T:
            newlist.remove(e)
    while len(d_list) == 0:
        e = newlist[random.randint(0, len(newlist))]
        for d in range(2 * e):
            if (e * d) % T == 1:
                d_list.append(d)
    d = random.choice(d_list)
    return e, d


def encrypt(e, N, letter):
    return (ord(letter) ** e) % N


def encrypt_message(e, N, message):
    newlist = []
    for letter in message:
        newlist.append(encrypt(e, N, letter))
    return newlist


def decrypt(N, d, encletter):
    return chr((encletter ** d) % N)


def decrypt_message(N, d, list):
    newstr = ""
    for encletter in list:
        newstr += decrypt(N, d, encletter)
    return newstr
