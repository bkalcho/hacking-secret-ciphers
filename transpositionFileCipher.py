# Author: Bojan G. Kalicanin
# Date: 26-Feb-2017
# Description: Using transposition cipher to encrypt/decrypt files.

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.txt'
    # BE CAREFUL! If a file with the outputFilename already exists,
    # this programm will overwrite that file.
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt' # Set to 'encrypt' or 'decrypt'

    # If the input file does not exist, then the program terminates
    # early.
    if not os.path.exists(inputFilename):
        print('The file {0:s} does not exist. Quitting...'.format(inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
        print('This will overwrite the file {0:s}. (C)ontinue or (Q)uit?'\
            .format(outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file.
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('{0:s}ing...'.format(myMode.title()))

    # Measure how logn the encryption/decryption takes.
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('{0:s}ion time: {1:f} seconds'.format(myMode.title(), totalTime))

    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done {0:s}ing {1:s} ({2:d} characters).'.format(myMode,
        inputFilename, len(content)))
    print('{0:s}ed file is {1:s}.'.format(myMode.title(), outputFilename))

if __name__ == '__main__':
    main()
