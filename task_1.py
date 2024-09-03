import random
import string

print("Password Generator!")

# Prompt the user to specify the desired length of the password
desired_length = int(input("Please specify the desired length of the password: "))

low = string.ascii_lowercase
upp = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Initialize the password
password = low + upp + num + symbols

# Iterate over each character in the password and shift it back by one position
decrypted_password = "".join(random.sample(password,desired_length))

# Print the decrypted password
print(f"The Generated Password is: {decrypted_password}")
