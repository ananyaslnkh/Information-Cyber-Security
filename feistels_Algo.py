#16 bit data

def Feistels_Encrypt(bits, key):
    L0 = (bits[0:len(bits)//2]) 
    R0 = (bits[len(bits)//2:])
    L1 = R0                                                 #assigning L1 to R0
    T = ""
    for b1, b2 in zip(R0, key):
        T = T + str(int(b1)|int(b2))                        #Generating T using OR
    R1 = ""
    for b1, b2 in zip(L0, T):
        R1 = R1 + str(int(b1)^int(b2)) 
    final = L1+R1

    return final

def Feistels_Decrypt(final, key):
    L1 = (bits[0:len(bits)//2])
    R1 = (bits[len(bits)//2:])
    R0 = L1
    T = ""
    for b1, b2 in zip(L1, key):
        T = T + str(int(b1)|int(b2))
    L0 = ""
    for b1, b2 in zip(T, R1):
        L0 = L0 + str(int(b1)^int(b2)) 
    final = L0+R0
    return final

bits = "1111000000001110"
key = "10101010"
print("Entry Bits: ",bits)
Encrypt = Feistels_Encrypt(bits, key)
print("Encrypted String: " ,Encrypt)
Decrypt = Feistels_Decrypt(Encrypt, key)
print("Decrypted String: " ,Decrypt)