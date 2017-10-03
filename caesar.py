# Script:  caesar.py
# Desc:    encrypt and decrypt text with a Caesar cipher
#          using defined character set with index
# Author:  Scott Bean
# Created: 23/9/17
"""The code for the frequency analysis in caesar_crack is adapted from
https://www.nayuki.io/res/automatic-caesar-cipher-breaker-javascript/automatic-caesar-cipher-breaker.js
;a javascript implimentation of the same function"""

import string, time, math
from operator import itemgetter

charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # characters to be encrypted

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
    print (f'[*] ciphertext: {ciphertext}\n')
    return ciphertext # returns ciphertext so it can be reused

def caesar_decrypt(ciphertext,key):
    """Will decrypt any cipher text with the given key"""
    # very similar to caesar_encrypt(), but shift left
    print (f'[*] DECRYPTING - key: {key}; ciphertext: {ciphertext}')

    plaintext=''

    # Remove spaces and upper case input
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace(" ","")

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

    print (f'[*] plaintext: {plaintext}\n')
    return plaintext # returns plaintext so it can be reused

def caesar_crack(ciphertext):
    """This function will crack any string it has been given"""
    print(f'[*] Bruteforce caesar cipher\n')

    # Get start time
    start_time = time.time()
    # Remove spaces and upper case input
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace(" ","")
    # This is a 2D array, totalEntropy is the 1st dimention
    totalEntropy = []

    for x in range(len(charset)):
        # second dimention of the totalEntropy array
        eachEntropy = []
        # Make a table to transform our charset
        crack_table = str.maketrans(charset, charset[x:]+charset[:x])
        # Apply the table to the sting
        cracked = ciphertext.translate(crack_table)

        # Build a list of the entropy, the shift postion and the cracked text
        eachEntropy.append(x)
        eachEntropy.append(entropyCalculation(cracked))
        eachEntropy.append(cracked)
        totalEntropy.append(eachEntropy)

    soultion = findSolution(totalEntropy)

    print("Elapsed time: %.3fs" % (time.time() - start_time))
    return soultion

def main():
    # test cases
    key=2
    plain1 = 'Hello Suzanne'
    cipher1 = 'IQQfOQtpKpIGXGtaQPG'
    crackme = 'PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA'
    # call functions with text cases
    caesar_encrypt(plain1, key)
    caesar_decrypt(cipher1,key)
    caesar_crack(crackme)  # remove comment to test cracking

def ui():
    """Displays the menu system"""
    print('\n######################################################')
    print('#                                                    #')
    print('#                   Caesar Cipher                    #')
    print('#                    Scott Bean                      #')
    print('#                       2017                         #')
    print('#                                                    #')
    print('######################################################\n')

    # Run the test case code?
    testCase = input("Do you want to run the test cases (Y/N)?\n")

    # Call main if the test cases should be run
    if "y" in testCase.lower():
        main()
    else:
        # Get the string and key/bruteforce
        text = input("Enter your string to be en/decrypted: ")
        key = input("Enter your key or ? to bruteforce: ")
        if "?" in key:
            # If we dont know the key, crack it
            caesar_crack(text)
        else:
            # Should we encrypt or decrypt this string?
            mode = input("Enter e to encrypt or d to decrypt: ")
            # Call correct function
            if "e" in mode.lower():
                caesar_encrypt(text,int(key))
            else:
                caesar_decrypt(text,int(key))

def entropyCalculation(ciphertext):
    """Calculates the entropy of the ciphertext"""

    # An array of frequencies of letters in the english language A-Z
    ENG_FREQUENCY = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406,
	0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

    # Total entropy
    totalE = 0

    # loop through the ciphertext
    for x in range(len(ciphertext)):
        # get the number position for each char to map to the ENG_FREQUENCY array
        index = string.ascii_uppercase.index(ciphertext[x])
        # Add the chars entropy to the total entropy for that word
        totalE += math.log(ENG_FREQUENCY[index])
    # returns a usable entropy value
    return -totalE / math.log(2) / len(ciphertext)

def findSolution(entropy):
    """Prints the answer with the lowest entropy"""
    # Sort the array by lowest entropy
    entropy = sorted(entropy, key=itemgetter(1))

    # Print the result
    print('Shift: ',entropy[0][0],' | ',entropy[0][2])
    print('------------------')

# boilerplate
if __name__ == '__main__':
    # Call the UI function as it will call all other methods
    ui()
