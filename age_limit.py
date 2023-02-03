# Problem
# Chef wants to appear in a competitive exam. To take the exam, there are following requirements:
# Minimum age limit is 
# X (i.e. Age should be greater than or equal to X).
# Age should be strictly less than 
# Y.
# Chef's current Age is 
# A. Find whether he is currently eligible to take the exam or not.

# Input Format
# First line will contain 
# T, number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing three integers ,
# X,Y, and 
# A as mentioned in the statement.

for i in range(int(input())):
    x,y,a = map(int,input().split())
    if x<=a<y and 10<=a<=50:
        print('yes')
    else:
        print('no')







