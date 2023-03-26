def hexToBin(hex):
    decimal = int(hex, 16)
    binary = bin(decimal)[2:]
    return binary

def xor(string1, string2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(string1,string2)])

cipher_hex ='1525053514291239'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def keys(a):
    
        return (a+"@"+a+"@"+a+"@"+a+"@")
    

def hex_to_text(hex_string):
    byte_string = bytes.fromhex(hex_string)
    plaintext = byte_string.decode('utf-8')
    return plaintext

def xor_reverse(key, ciphertext):
    plaintext = xor(key, ciphertext)
    return plaintext

with open('common_words.txt') as f:                                                
    com_words = set(f.read().split())  

for i in range (len(alphabet)):
    cipherCode = hex_to_text(cipher_hex)# ciphercode in string format 
    a = alphabet[i]
    key = keys(a) #key
    #key_bin = hexToBin(key)
    #cipher_bin = hexToBin(cipher_hex)
    plaintext = xor(key, cipherCode)
    if plaintext in com_words:
     print(plaintext)
     break