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
    plaintext = plaintext.replace(" ", "") # Remove all spaces from string
    ciphertext=''    # initialise ciphertext as empty string

    for ch in plaintext: #Loop through ever char in the plaintext
        if ch in charset:
            # Index is the int positon in the alphabet 0-25
            index = string.ascii_uppercase.index(ch)

            # Shift indicates how many places we have moved - a counter
            shift = 0

            # Keep shifting untill we hit the required amount of shifts
            while shift != key+1:
                # Get the new char
                ch = string.ascii_uppercase[index]
                # check to see where in the charset we are
                if index == len(charset):
                    # If we are at the end we need to loop back to the start
                    index = 0
                else:
                    # Otherwise we can continue as normal
                    index += 1
                shift += 1


            new = ch
        else:
            new=ch # do nothing with characters not in charset
        ciphertext=ciphertext+new
    print (f'[*] ciphertext: {ciphertext}')
    return ciphertext # returns ciphertext so it can be reused

def caesar_decrypt(ciphertext,key):
    """put an appropriate function doc string here"""
    # very similar to caesar_encrypt(), but shift left
    print (f'[*] DECRYPTING - key: {key}; ciphertext: {ciphertext}')
    #
    plaintext=''   # replace this with your code
    #
    print (f'[*] plaintext: {plaintext}')
    return plaintext # returns plaintext so it can be reused

def caesar_crack(ciphertext):
    """put an appropriate function doc string here"""
    # how could you brute force crack a caesar cipher?
    # your code here


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
    caesar_encrypt("This is a test sentence",4)
