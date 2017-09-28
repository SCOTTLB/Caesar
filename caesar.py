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

    plaintext=plaintext.upper()     # convert plaintext to upper case
    ciphertext=''    # initialise ciphertext as empty string

    for ch in plaintext:
        if ch in charset:
            # Index is the int positon in the alphabet 0-25
            index = string.ascii_uppercase.index(ch)

            # Shift indicates how many places we have moved - a counter
            shift = 0

            # Keep shifting untill we hit the required amount of shifts
            while shift != key+1:
                # Loop when reaching the end of the charset
                if index + key > 25:
                    # TODO: what happens at the end
                    print("looping")
                    break
                else:
                    # not going to hit the end opf the charset
                    ch = string.ascii_uppercase[index]
                    shift += 1
                    index += 1
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
    caesar_encrypt("abcd",7)
