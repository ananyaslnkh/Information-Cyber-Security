def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():                      # makes sure only letters are encrypted, skipping spaces, punctuations and other characters
            shift_amount = shift % 26           # shift wraps around if its greater than 26 (bcs there are 26 letters)
            #print(shift_amount)
            code = ord(char) + shift_amount     # ord gives the ascii value of the character
            #print(code)
            if char.islower():                  # if char is lowercase and if code ie ascii val of char is > ascii val of z then wrap around to the beginning of the lowercase alphabet
                if code > ord('z'):
                    code -= 26
            elif char.isupper():                # if char is uppercase and if code of char is > ascii val of Z then wrap around to the beginning of uppercase alphabet
                if code > ord('Z'):
                    code -= 26
            encrypted_text += chr(code)         # adding encrypted character to the result and converting ascii code back to char
        else:
            encrypted_text += char              # handling non alphabetic characters
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            code = ord(char) - shift_amount
            if char.islower():
                if code < ord('a'):
                    code += 26
            elif char.isupper():
                if code < ord('A'):
                    code += 26
            decrypted_text += chr(code)
        else:
            decrypted_text += char
    return decrypted_text


plaintext = "This is my ICS assignment number one"
shift = 26
ciphertext = encrypt_caesar(plaintext, shift)
print(f"Encrypted: {ciphertext}")

decrypted_text = decrypt_caesar(ciphertext, shift)
print(f"Decrypted: {decrypted_text}")