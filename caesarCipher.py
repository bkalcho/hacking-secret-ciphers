# Author: Bojan G. Kalicanin
# Date: 15-Feb-2017
# Description: Implementation of the Caesar Cipher

import paperclip

message = 'This is my secret message.'
# The encryption/decryption key
key = 13
# Mode of the program: encrypt/decrypt
mode = 'encrypt'
# Symbols that can be encrypted
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Store encrypted/decrypted form of the message
translated = ''
# Capitalize the string in a message
message = message.upper()

# Run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in letters:
        # Get the encrypted (or decrypted) number for this symbol
        num = letters.find(symbol) # Get the number of the symbol
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key
        
        # Handle the wrap-around if num is larger than the length of
        # letters or less than 0
        if num >= len(letters):
            num -= len(letters)
        elif num < 0:
            num += len(letters)
        
        # Add encrypted/decrypted number's symbol at the end of translated
        translated += letters[num]

    else:
        # Just add the symbol without encrypting/decrypting
        translated += symbol

# Print encrypted/decrypted string to the screen
print(translated)

# Copy the encrypted/decrypted string to the clipboard
paperclip.copy(translated)
