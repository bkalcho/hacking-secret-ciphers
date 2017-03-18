# Author: Bojan G. Kalicanin
# Date: 18-Mar-2017
# Description: Encryption program using Affine cipher

import sys, paperclip, cryptomath, random

symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    myMessage = """"A computer would deserve to be called intelligent if it
    could deceive a human into believing that it was human." -Alan Turing"""
    myKey = 2023
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: {0:d}'.format(myKey))
    print('{0:s}ed text:'.format(myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full {0:s}ed text copied to clipboard.'.format(myMode))


def getKeyParts(key):
    keyA = key // len(symbols)
    keyB= key % len(symbols)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is \
            set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes icredibly weak when key B is \
            set to 0. Choose a different key.')
    if keyA < 0 and keyB < 0 or keyB > len(symbols) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 \
            and {0:d}.'.format(len(symbols) - 1))
    if cryptomath.gcd(keyA, len(symbols)) != 1:
        sys.exit('Key A ({0:d}) and the symbol set size ({1:d}) are not \
            relatively prime. Choose a different key.'.format(keyA, len(symbols)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in symbols:
            # encrypt this symbol
            symIndex = symbols.find(symbol)
            cyphertext += symbols[(symIndex * keyA + keyB) % len(symbols)]
        else:
            ciphertext += symbol # just append this symbol unencrypted
    return ciphertext


def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(symbols))

    for symbol in message:
        if symbol in symbols:
            # decrypt this symbol
            symIndex = symbols.find(symbol)
            plaintext += symbols[(symIndex - keyB) * modInverseOfKeyA % \
                len(symbols)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext


def getRandomKey():
    while True:
        keyA = random.randint(2, len(symbols))
        keyB = random.randint(2, len(symbols))
        if cryptomath.gcd(keyA, len(symbols)) == 1:
            return keyA * len(symbols) + keyB


if __name__ == '__main__':
    main()
