
def calculate_public_key(p, q):
    return p * q


def encrypt(n, e, letter):
    return (ord(letter) ** e) % n


def encrypt_message(n, e, message):
    newlist = []
    for i in message:
        newlist.append(encrypt(n, e, i))
    return newlist


def calculate_private_key(p, q):
    return (p - 1) * (q - 1)



def decrypt(p, q, r):
    return (r ** calculate_private_key(p, q)) % calculate_public_key(p, q)


print(encrypt(calculate_public_key(3, 5), 69, "a"))
print(chr((decrypt(3, 5, 6))))
