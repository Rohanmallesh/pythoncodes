# Problem
# Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.
# Relational Operators are operators which check relationship between two values. Given two numerical values A and B you need to help chef in finding the relationship between them that is,

# First one is greater than second or, First one is less than second or, First and second one are equal.
 

# Input
# First line contains an integer T, which denotes the number of testcases. Each of the T lines contain two integers A and B.

for i in range(int(input())):
    a,b = map(int , input().split())
    if a == b:
        print('=')
    elif a>b:
        print('>')
    else:
        print('<')


