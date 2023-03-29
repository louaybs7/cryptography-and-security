
def indexOfLetter(letter):
    for i in range (len(alphabet)):
        if alphabet[i]==letter:
            return i
        
    return alphabet.index(letter)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def letterOfIndex(index):
    return alphabet[index]

def shift_left(letter,shift):
    i=indexOfLetter(letter)
    new = (i-shift)%26
    return letterOfIndex(new)

def BruteForcing (ch):
    for shift in range (26):
        ret=""
        for c in ch :
            new = shift_left(c,shift)
            ret=ret+new
        print ("[",shift,"]",ret)
         

BruteForcing("lsal") 




    
           

      
   