# Script:  caesar.py
# Desc:    encrypt and decrypt text with a Caesar cipher
#          using defined character set with index
# Author:  Petra Leimich
# Created: 23/9/17
# note that you should add a module doc string!

import string

charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # characters to be encrypted
numchars=len(charset) # number of characters, for wrapping round

def caesar_encrypt(plaintext,key):
    """Will encrypt any plain text using the key provided"""
    print (f'[*] ENCRYPTING - key: {key}; plaintext: {plaintext}')

    plaintext=plaintext.upper()    # convert plaintext to upper case
   # plaintext = plaintext.replace(" ", "") # Remove all spaces from string
    ciphertext=''    # initialise ciphertext as empty string

    for ch in plaintext: #Loop through ever char in the plaintext
        if ch in charset:
            # Index is the int positon in the alphabet 0-25
            index = string.ascii_uppercase.index(ch)

            # Shift indicates how many places we have moved - a counter
            shift = 0

            # Keep shifting untill we hit the required amount of shifts
            while shift != key+1:
                
                # check to see where in the charset we are
                if index == len(charset)-1:
                    # If we are at the end we need to loop back to the start

                    # Get the new char
                    ch = string.ascii_uppercase[index]
                    # Set our pointer back to the start of the alphabet
                    index = 0
                else:
                    # Otherwise we can continue as normal

                    # Get the new char
                    ch = string.ascii_uppercase[index]
                    # Advance the pointer one letter
                    index += 1
                # Add one to that counter!
                shift += 1
            # Save the new char
            new = ch
        else:
            new=ch # do nothing with characters not in charset
        ciphertext=ciphertext+new
    print (f'[*] ciphertext: {ciphertext}')
    return ciphertext # returns ciphertext so it can be reused

def caesar_decrypt(ciphertext,key):
    """Will decrypt any cipher text with the given key"""
    # very similar to caesar_encrypt(), but shift left
    print (f'[*] DECRYPTING - key: {key}; ciphertext: {ciphertext}')

    plaintext=''

    # Sanity check input, ensure its formatted properly
    ciphertext = ciphertext.upper()
   # ciphertext.replace(" ","")

    # loop through all the letters
    for ch in ciphertext:
        if ch in charset:
            # Need a counter
            shift = key

            # Get alphabetical position of ch
            index = string.ascii_uppercase.index(ch)

            # Do we still have places to move?
            while shift > -1:
                # assign the new char
                ch = string.ascii_uppercase[index]
                if index == 0:
                    
                    index = len(charset)-1
                else:
                    index -= 1

                shift -= 1
            new=ch
        else:
            # Preserve spaces
            new=ch
        plaintext=plaintext+new   # hold the output

    print (f'[*] plaintext: {plaintext}')
    return plaintext # returns plaintext so it can be reused

def caesar_crack(ciphertext):
    """This function will crack any string it has been given"""
    print(f'[*] Bruteforce caesar cipher\n')
    for x in range(len(charset)):
        
        # Make a table to transform our charset
        crack_table = str.maketrans(charset, charset[x:]+charset[:x])
        # Apply the table to the sting
        cracked = ciphertext.translate(crack_table)

        # Make the output table pretty
        if x > 9:
            spacer = ''
        else:
            spacer = ' '

        print('Shift: ',x,spacer,'| ',cracked)
        print('------------------')

def main():
    # test cases
    key=2
    plain1 = 'Hello Suzanne'
    cipher1 = 'IQQfOQtpKpIGXGtaQPG'
    crackme = 'PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA'
    # call functions with text cases
    caesar_encrypt(plain1, key)
    caesar_decrypt(cipher1,key)
    # caesar_crack(crackme)  # remove comment to test cracking

# boilerplate
if __name__ == '__main__':
    caesar_crack('PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA')
   # caesar_encrypt("this is a test case string with spaces", 5)
   # caesar_decrypt("YMNX NX F YJXY HFXJ XYWNSL BNYM XUFHJX", 5)
