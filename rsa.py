from prime import generate_prime
from gcd import gcd

e = 65537

def generate_keys():
    p = generate_prime(64)
    q = generate_prime(64)
    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime")

    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(M: int, public_key):
    e, n = public_key
    C = pow(M, e, n)
    return C

def decrypt(C: int, private_key):
    d, n = private_key
    M = pow(C, d, n)
    return M
