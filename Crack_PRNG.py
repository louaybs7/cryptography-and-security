

import functools
import math
''' To solve this i did three steps: 
1-First i found the key using the xor function and the cipher code and the plaintext
2-Then i put the key in an array with all generated code which they are the ascii code of the key caracters
3-Then i used the crack PRNG methode with all the fucntions (crack_increment/crack_multpiler/crack_modulus) to find the modulus, increment and multiplier of the PRNG'''
# -------------------Finding the key -------------------#


def hex_to_text(hex_string):
    byte_string = bytes.fromhex(hex_string)
    plaintext = byte_string.decode('utf-8')
    return plaintext


def xor(string1, string2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string1, string2)])


txt = 'cybersecurity'
cipher_hex = '62716b6b777862677362667e7b'

key = (xor('cybersecurity', hex_to_text(cipher_hex)))
# -------------------put the key in an array with all generated codes -------------------#

array_key = []
for i in range(len(key)):
    array_key.append(ord(key[i]))
# -------------------Crack PRNG-------------------#


def crack_increment(States, modulus, multiplier):
    increment = (States[1] - States[0] * multiplier) % modulus
    return increment


def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def crack_multpiler(States, modulus):
    multiplier = (States[2] - States[1]) * \
        modinv(States[1] - States[0], modulus) % modulus
    increment = crack_increment(States, modulus, multiplier)
    return multiplier, increment


def crack_modulus(States):
    diffs = [s1 - s0 for s0, s1 in zip(States, States[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(functools.reduce(math.gcd, zeroes))
    increment, multiplier = crack_multpiler(States, modulus)
    print('modulus=', modulus, ', increment=',
          increment, ', multiplier= ',  multiplier)


# print(crack_modulus(array_key))
crack_modulus(array_key)
