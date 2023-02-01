# Problem
# You're given an integer N. Write a program to calculate the sum of all the digits of N.

# Input Format
# The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.
# p = input()
for i in range(int(input())):
    ans = 0
    n = input()
    for j in str(n):
       ans += int(j)
    print(ans)
    