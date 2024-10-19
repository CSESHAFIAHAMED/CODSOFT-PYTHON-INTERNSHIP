import random
import string


print("Password Generator")
print("------------------")

password_length = int(input("Enter the desired password length: "))
def generate_password(length):
  
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  special_chars = string.punctuation

  
  all_chars = lowercase + uppercase + digits + special_chars

  
  password = ''.join(random.choice(all_chars) for _ in range(length))

  return password


password = generate_password(password_length)


print("Generated Password: ", password)