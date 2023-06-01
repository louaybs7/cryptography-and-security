
from filecmp import cmp
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import hashlib 
import secrets



#-----------------sender fucntions -----------------------------
def mypad(s):
    Block_size=16
    padding_length = Block_size - len(s) % Block_size  # Calculate the amount of padding needed
    pad = bytes([padding_length] * padding_length)  # Determine the padding byte
    return s+pad.decode()  # Return the padded message 

def encrypt_AES_CBC(plaintext, key):
    iv = secrets.token_bytes(16) # Generate a random IV
    Enc = AES.new(key, AES.MODE_CBC, iv=iv)  # Create a new AES cipher object in CBC mode with the key and IV
    data = mypad(plaintext).encode()  # Pad the plaintext to a multiple of the block size
    ciphertext = Enc.encrypt(data)  # Encrypt the padded plaintext using the cipher
    ciphertext_hex =iv.hex()+ciphertext.hex()  
    return ciphertext_hex  # Return the concatenation of the IV and ciphertext in hex format


# hash function   
def hash_function(in_str):   
    in_bytes = in_str.encode()
    hash_obj = hashlib.sha1(in_bytes)
    hash_str = hash_obj.hexdigest()
    return hash_str



def sender(key):

 with open('message.txt') as f:                                                
    txt = f.read()
    original_hash_code = hash_function(txt)
    ciphertext= encrypt_AES_CBC(txt,key)
    return ciphertext,original_hash_code

#-----------------receiver fucntions -----------------------------

def myunpad(s):
    return s[:-ord(s[len(s)-1:])]


def decrypt_AES_CBC(ciphertext,key):
 iv = secrets.token_bytes(16) # Extract the IV
 ciphertext = bytes.fromhex(ciphertext[32:])
 decrypted_plaintext= AES.new(key, AES.MODE_CBC, iv=iv) #new cipher object 
 plaintext = decrypted_plaintext.decrypt(ciphertext)
 return plaintext


def compare_strings(s1, s2):
    if s1 == s2:
        print("the hash code is the same")
    else:
        print("the hash code is not the same")
        

# receiver function
def receiver(ciphertext, hash, key):
    hash_new = hash_function(ciphertext)
    if hash_new == hash:
        print("The plaintext is: ", ciphertext)
        print("\nHashes match, message is authentic")
        plaintext = decrypt_AES_CBC(ciphertext, key)
        print("Decrypted message: ", plaintext)
    else:
        print("Hashes don't match, message is not authentic")
    
   
#-----------------main fucntions -----------------------------

def main():
    with open('message.txt') as f:                                                
     txt = f.read()
    key = (secrets.token_hex(16)).encode("utf-8")
    print("the key is : "+key.decode()+"\n")
    cipher,hash=sender(key)
    print("-------------------------\n")
    print("the message is : "+txt+"\n")
    print("-------------------------\n")
    print("the hash value : "+hash+"\n")
    print("-------------------------\n")
    print("the cipher_txt: "+ cipher+"\n")
    print("-------------------------\n")
    print(receiver(hash,cipher,key))

if __name__ == "__main__":
    main()

