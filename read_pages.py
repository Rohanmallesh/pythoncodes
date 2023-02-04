# Problem
# Chef has started studying for the upcoming test. The textbook has 
#  N pages in total. Chef wants to read at most X pages a day for Y days.
# Find out whether it is possible for Chef to complete the whole book.

# Input Format
# The first line of input will contain a single integer 
# T, denoting the number of test cases.
# The first and only line of each test case contains three space-separated integers 
# ,N,X, and Y — the number of pages, the number of pages Chef can read in a day, and the number of days.

for i in range(int(input())):
    n,x,y = map(int,input().split())
    if x*y >= n:
        print('YES')
    else:
        print('NO')




