# Author: Bojan G. Kalicanin
# Date: 25-Feb-2017
# Description: Tester program for transposition cipher program.

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42) # Set the random "seed" to a static value
    for i in range(20): # Run 20 tests
        # Generate random messages to test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        
        # Convert the message string to a list to shuffle it.
        message = list(message)
        random.shuffle(message)

        message = ''.join(message) # Convert list to string
        print('Test #{0:d}: "{1:s}..."'.format(i+1, message[:50]))

        # Check all possible keys for each message.
        for key in range(1, len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # If the decryption doesn't match the original message,
            # display an error message and quit.
            if message != decrypted:
                print('Missmatchwith with key {0:s} and message {1:s}.'\
                    .format(key, message))
                print(decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

# If transpositionTest.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
