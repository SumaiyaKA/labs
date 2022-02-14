# Program to implement Caesar Cipher and Vigeneré Cipher

# Encryption Caesar Cipher [1] in menu
def enc_caesar(origin, key):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    origin = origin.upper()
    translated = ""
    for symbol in origin:
        if symbol in LETTERS:
            index = (LETTERS.find(symbol) + key) % len(LETTERS)
            translated += LETTERS[index]
        else:
            translated += symbol
 
    return translated

# Decryption Caesar Cipher [2] in menu
def de_caesar(encrypted_text):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in encrypted_text:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated += LETTERS[num]
            else:
                translated += symbol
        print('\n\nHacking key #%s:\n%s' % (key, translated))

# To make the key same length as the message
def get_key(origin, key):
    # generate the key for encryption 
    key = list(key)
    if len(origin) == len(key):
        return(key)
    else:
        for i in range(len(origin) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key)) 


# Encryption Vigeneré Cipher
def enc_vigeneré(origin, key):
    key = get_key(origin, key)
    # encrypt the original text using the key 
    cipher_text = []
    for i in range(len(origin)):
        x = (ord(origin[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    translated = "" . join(cipher_text)
    return(translated)

# Encryption Vigeneré Cipher
def de_vigeneré(encrypted_text, key):
    cipher_text = []
    key = get_key(encrypted_text, key)

    for i in range(len(encrypted_text)):
        x = (ord(encrypted_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    translated = "" . join(cipher_text)
    return(translated)

def display(origin, key, translated):
    print ("\n\nOriginal text  : " + origin)
    print ("\nShifted by : " + str(key))
    print ("\nTranslated text: " + translated)

def menu():
    user_reply = 10
    # while(user_reply != 0):
    print("\n.........................................................")
    print("\nSelect a process:")
    print("\n1. Caesar Cipher Encryption.")
    print("\n2. Caesar Cipher Decryption without key.")
    print("\n3. Vigeneré Cipher Encryption.")
    print("\n4. Vigeneré Cipher Decryption.")
    print("\n5. Find Key of Caesar Cipher Encryption key.")
    print("\n0. Exit")
    print("\n.........................................................\n")
    user_reply = input('Enter the number of your selection: ')
    if(user_reply == '1'):
        origin = input('Enter text to encrypt it: ')
        key = input('Enter the key (integer): ')
        translated = enc_caesar(origin, int(key))
        display(origin, key, translated)
    if(user_reply == '5' or user_reply == '2'):
        encrypted_text = input('Enter the encrypted text: ')
        de_caesar(encrypted_text)
    if(user_reply == '3'):
        origin = input('Enter text to encrypt it: ')
        key = input('Enter the key (word): ')
        translated = enc_vigeneré(origin, key)
        display(origin, key, translated)
    if(user_reply == '4'):
        encrypted_text = input('\nEnter the encrypted text: ')
        key = input('\nEnter the key (word): ')
        origin = de_vigeneré(encrypted_text, key)
        display(origin, key, encrypted_text)
    

if __name__ == "__main__":
    # example: ATTACKATONCE

    menu()




