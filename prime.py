from random import randint, getrandbits

def is_prime(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    # Tulis n-1 sebagai d * 2^s
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    # Uji primalitas Miller-Rabin
    for _ in range(k):
        a = randint(2, min(n-2, 1 << 20))
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        p = getrandbits(bits)
        p |= (1 << (bits - 1)) | 1  # Pastikan bit tertinggi 1 dan ganjil
        if is_prime(p):
            return p
