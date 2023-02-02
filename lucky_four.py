# Problem
# You are given a list of T integers, for each of them you have to calculate the number of occurrences of the digit 4 in the decimal representation.

# Input
# The first line of input consists of a single integer T, denoting the number of integers in the list.
# Then, there are T lines, each of them contain a single integer from the list.

for i in range(int(input())):
    k = int(input())
    count = 0
    while k:
        if k%10 == 4:
            count += 1
        k = int(k/10)
    print(count)



