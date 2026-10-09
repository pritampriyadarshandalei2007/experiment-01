#wap to enter two numbers and swap them using bitwise operators.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("First number =", a)
print("Second number =", b)