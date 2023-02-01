# Problem
# You are given N integers. Find the count of numbers divisible by K.
# Input Format
# The input begins with two positive integers N, K. The next N lines contains one positive integer each denoted by Ai.

n,k = map(int,input().split())
t = 0
for i in range(n):
    p = int(input())
    if p%k == 0:
        t += 1
print(t)     



