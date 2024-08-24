'''
Logic:

We first split the data into 2 halves left and right
Then a round function is applied to one half of the data(usually the right half) & 
then combined with the other half using XOR
The halves are then swapped for the next round
'''

def Feistels_Encrypt(bits, key):
    L0 = bits[0:len(bits)//2]   # splitting the input 
    R0 = bits[len(bits)//2:]
    L1 = R0                     # the left half for the next round becomes the curr right half
    T = ""
    for b1, b2 in zip(R0, key):
        T += str(int(b1) | int(b2))  # Generating T using OR  

# By XORing, transformation of the left half (L0) combined with 
# the transformed right half (T) produces the new right half (R1)
    R1 = ""
    for b1, b2 in zip(L0, T):
        R1 += str(int(b1) ^ int(b2))  # Generating R1 using XOR
    final = L1 + R1
    return final

def Feistels_Decrypt(final, key):
    L1 = final[0:len(final)//2]
    R1 = final[len(final)//2:]
    R0 = L1             # reversing the swap
    T = ""
    for b1, b2 in zip(R0, key):
        T += str(int(b1) | int(b2))
    L0 = "" 
    for b1, b2 in zip(T, R1):
        L0 += str(int(b1) ^ int(b2))        # recovering L0 using XOR
    bits = L0 + R0          # this gives final decrypted binary string
    return bits

def BinaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return (decimal)

def binary_to_Str(bits):
    L0 = int(bits[0:len(bits)//2])
    R0 = int(bits[len(bits)//2:])
    L1 = BinaryToDecimal(L0)
    R1 = BinaryToDecimal(R0)
    Final = chr(L1)+chr(R1)
    return Final

string = "PA"
bits = ''.join(format(ord(i), '08b') for i in string)
key = "10101010"
print("Entry Bits: ", bits)
Encrypt = Feistels_Encrypt(bits, key)
print("Encrypted Code: ", Encrypt)
Str_Encrypt = binary_to_Str(Encrypt)
print("Encrypted_String: ", Str_Encrypt)
Decrypt = Feistels_Decrypt(Encrypt, key)
print("Decrypted String: ", Decrypt)
Str_Decrypt = binary_to_Str(Decrypt)
print("Decrypted_String: ", Str_Decrypt)