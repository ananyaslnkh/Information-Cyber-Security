import hashlib
str = "Hello, I am Ananya"

print("Message is: " + str)
print ("\r")

result = hashlib.sha1(str.encode())  # str.encode() converts the string to a bytes object, as the hashlib functions require a bytes like object as input

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())   # returns the hash value as a hexadecimal string
print ("\r")