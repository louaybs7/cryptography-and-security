import random

inp = input("Enter a string: ")

#give u the index of a letter in the alphabet
def indexOfLetter(letter):
    for i in range (len(alphabet)):
        if alphabet[i]==letter:
            return i
        
    return alphabet.index(letter)

alphabet = 'abcdefghijklmnopqrstuvwxyz, '
#give u the letter of a index in the alphabet
def letterOfIndex(index):
    return alphabet[index]

def shift_left(letter,shift):
    i=indexOfLetter(letter)
    new = (i-shift)%28
    return letterOfIndex(new)

def shift_right(letter,shift):
    i=indexOfLetter(letter)
    new = (i+shift)%28
    return letterOfIndex(new)



def createKey (length):
    key=[]
    for i in range (length):
        key=key+[random.randint(0,25)]
    return key


keys = createKey(len(inp)) #create a key with the same length of the input

def encrypt(plaintext):
    
    code = ""
    for i in range (len(plaintext)):
        code=code+shift_right(plaintext[i],keys[i])
    return code 
    
    

def decrypt(code):
    txt=""
    for i in range (len(code)):
        txt=txt+shift_left(code[i], keys[i])
    return txt


print("txt encrypted :",encrypt(inp))
print("txt decrypted :",decrypt(encrypt(inp)))




    
           

      
   