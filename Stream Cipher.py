"""
To solve this problem :
1-I first read the line from the file character by character
2-I took each character then create the char_key related to it randomly using the LFSR and i use the char it selfe as a seed so i will have a different and secret key for each character.
3-Then I took that char_key and XOR it  with the character that we want to encrypt it.
4- After all this I will have a xor_result thta i will append it to the final key.
5-I repeat this for the whole characters in the file.
6-for decryption I use the xor decryption using the total key that i already saved from the above process then i XOR it with the cipher code so I have the Plaintext as 
result in the end .

After Running the given example :
The cipher code :(D»(»(((ï×ÿ(|«(((((|(ï×((ï«×ïï×((××ï×»Ç
The plaintext is :this is a stream of data to be transferred securely.
"""
# ---------------------------------------FINDING THE KEY/method using different seed for each char ---------------------------------------
def binary_string_to_string(binary_string):
    return ''.join(chr(int(binary_string[i*8:i*8+8], 2)) for i in range(len(binary_string)//8))


def lfsr_generator(seed, mask, n):
    seed = int(seed, 2)
    mask = int(mask, 2)
    key = ''

    for i in range(n):
        feedback = 0
        for j in range(n):
            if mask & (1 << j):
                feedback ^= (seed >> j) & 1
        seed = (seed >> 1) | (feedback << 7)
        key += str(feedback)

    return (key)


def xor(string1, string2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string1, string2)])


def read_char_and_return_key():  
    cipher_code = ""
    total__key = ""
    mask = '10000011'
    with open("data_stream.txt", "r") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            # i convert the char to binary string and i uses it as a seed do i will have different key for each char
            char_seed = format(ord(c), '08b')
            # after i regenerate the key i convert it to string so i can use it in xor function
            char_key = binary_string_to_string(
                lfsr_generator(char_seed, mask, 8))
            total__key = total__key+char_key
            xor_result = xor(char_key, c)  # i xor the key with the cipher code
            # i add the result to the cipher code so i will have the whole cipher code after addes all the chars code
            cipher_code += xor_result

    return cipher_code, total__key


def xor_decrypt(cipher_code, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(cipher_code, key)])


def main():
    txt = "this is a stream of data to be transferred securely."
    code, total__key = read_char_and_return_key()
    print("The cipher code :"+ code)
    plaintext = xor_decrypt(code, total__key)
    print("The plaintext is :"+ plaintext)
    

if __name__ == "__main__":
    main()
