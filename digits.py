number = int(input("Enter a number: "))

sum_digits = 0

while number > 0:
    digit = number % 10
    sum_digits = sum_digits + digit
    number = number // 10

print("Sum of digits =", sum_digits)