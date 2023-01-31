# Problem
# Chef's phone shows a Battery Low notification if the battery level is 15% or less.
# Given that the battery level of Chef's phone is 
# X%, determine whether it would show a Battery low notification.

# Input Format
# First line will contain T, number of test cases. Then the test cases follow.
# Each test case contains a single line of input, an integer X, denoting the battery level of the phone.

for i in range(int(input())):
    x = int(input())
    if x<=15:
        print('yes')
    else:
        print('no')