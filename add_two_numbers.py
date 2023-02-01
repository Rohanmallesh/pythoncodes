# Problem
# Problem Statement
# The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

# Input Format
# The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.

for i in range(int(input())):
    a,b = map(int,input().split())
    k = a+b
    print(k)

