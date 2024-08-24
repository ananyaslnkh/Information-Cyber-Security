import hashlib
str = "Hello World"

print("Message is: " + str)
print ("\r")

result = hashlib.sha1(str.encode()) 

print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())  
print ("\r")
