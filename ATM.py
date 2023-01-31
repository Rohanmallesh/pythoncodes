# Problem
# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, 
# and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). 
# For each successful withdrawal the bank charges 0.50 $US.
# Calculate Pooja's account balance after an attempted transaction.

# Input Format
# Each input contains 2 integers X and Y.
# X is the amount of cash which Pooja wishes to withdraw.
# Y is Pooja's initial account balance.

# Output Format
# Output the account balance after the attempted transaction, given as a number with two digits of precision.
# If there is not enough money in the account to complete the transaction, output the current bank balance.

x,y = map(float , input().split())
x = int(x)
if x +0.5<y and x%5==0:
     print(y-(x+0.5))
else:
    print(y)