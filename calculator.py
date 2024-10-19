def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  if y == 0:
    return "Error: Division by zero!"
  return x / y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Enter your choice (1/2/3/4): "))


if operation == 1:
  result = add(num1, num2)
elif operation == 2:
  result = sub(num1, num2)
elif operation == 3:
  result = mul(num1, num2)
elif operation == 4:
  result = div(num1, num2)
else:
  result = "Error: Invalid operation choice!"


print("Result: ", result)