# Problem
# Write a program to find the remainder when an integer A is divided by an integer B.

# Input
# The first line contains an integer T, the total number of test cases. Then T lines follow, each line contains two Integers A and B.

for i in range(int(input())):
    a,b = map(int,input().split())
    print(a%b)


