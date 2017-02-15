# Author: Bojan G. Kalicanin
# Date: 14-Feb-2017
# Description: Encryption of the message using Reverse cipher

message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

print(translated)
# Alternatively we can use slicing:
#print(message[-1::-1])
