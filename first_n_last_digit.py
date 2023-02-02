# Problem
# If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.

# Input Format
# The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N.

for i in range(int(input())):
    k = input()
    t = int(k[0]) + int(k[-1])
    print(t)

