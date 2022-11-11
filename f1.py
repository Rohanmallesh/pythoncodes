num = 1234
reversed_num = 0
Sum = 0
while num != 0:
digit = num % 10
Sum = Sum + digit
reversed_num = reversed_num * 10 + digit
num //= 10
print("Reversed Number: " + str(reversed_num))
print("The sum of digits", Sum)