# Author: Bojan G. Kalicanin
# Date: 16-Feb-2017
# Description: Hacking Caesar Cipher using brute-force technique.

message = 'GUVF VF ZL FRPERG ZRFFNTR.'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible possible key
for key in range(len(letters)):
    translated = ''

    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol)
            num -= key
            if num < 0:
                num += len(letters)
            
            translated += letters[num]
        
        else:
            translated += symbol
    
    print('Key #{0:d}: {1:s}'.format(key, translated))
