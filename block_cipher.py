from filecmp import cmp
from Crypto.Cipher import AES
import os
import hashlib
import secrets


# -----------------sender fucntions -----------------------------
def mypad(s):
    Block_size = 16
    # Calculate the amount of padding needed
    padding_length = Block_size - len(s) % Block_size
    # Determine the padding byte
    pad = bytes([padding_length] * padding_length)
    return s+pad.decode()  # Return the padded message


def encrypt_AES_CBC(plaintext, key):
    iv = secrets.token_bytes(16)  # Generate a random IV
    # Create a new AES cipher object in CBC mode with the key and IV
    Enc = AES.new(key, AES.MODE_CBC, iv)
    # Pad the plaintext to a multiple of the block size
    data = mypad(plaintext).encode()
    # Encrypt the padded plaintext using the cipher
    ciphertext = Enc.encrypt(data)
    ciphertext_hex = iv.hex()+ciphertext.hex()
    return ciphertext_hex  # Return the concatenation of the IV and ciphertext in hex format


def generate_hash(input_string):
    input_bytes = input_string.encode()
    hash_object = hashlib.sha1(input_bytes)
    hash_string = hash_object.hexdigest()

    return hash_string


def sender(key):

    with open('message.txt') as f:
        txt = f.read()
        original_hash_code = generate_hash(txt)
        ciphertext = encrypt_AES_CBC(txt, key)
        return ciphertext, original_hash_code

# -----------------receiver fucntions -----------------------------


def myunpad(s):
    return s[:-ord(s[len(s)-1:])]


def decrypt_AES_CBC(ciphertext, key):
    iv = secrets.token_bytes(16)  # Extract the IV
    ciphertext = bytes.fromhex(ciphertext[32:])
    decrypted_plaintext = AES.new(
        key, AES.MODE_CBC, iv)  # new cipher object
    plaintext = decrypted_plaintext.decrypt(ciphertext)
    return plaintext


def compare_strings(s1, s2):
    if s1 == s2:
        print("the hash code is the same")
    else:
        print("the hash code is not the same")


def receiver(original_hash, ciphertext, key):

    plaintext = decrypt_AES_CBC(ciphertext, key)
    snd_hash_code = generate_hash(plaintext.decode('latin-1'))
    compare_strings(original_hash, snd_hash_code)


# -----------------main fucntions -----------------------------

def main():
    with open('message.txt') as f:
        txt = f.read()
    key = (secrets.token_hex(16)).encode("utf-8")
    cipher, hash = sender(key)
    print("-------------------------\n")
    print("the message is : "+txt+"\n")
    print("-------------------------\n")
    print("the hash value : "+hash+"\n")
    print("-------------------------\n")
    print("the cipher_txt: " + cipher+"\n")
    print("-------------------------\n")
    print(receiver(hash, cipher, key))


if name == "main":
    main()
