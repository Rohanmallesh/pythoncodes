# Chef has been participating regularly in rated contests but missed 
# the last two contests due to his college exams. He now wants to solve 
# them and so he visits the practice page to view these problems.

# Given a list of 
# N contest codes, where each contest code is either START38 or LTIME108, 
# help Chef count how many problems were featured in each of the contests.

# Input Format
# First line will contain 
# T, number of test cases. Then the test cases follow.
# Each test case contains of two lines of input.
# First line of input contains the total count of problems that appeared in the two recent contests - 
# N. Second line of input contains the list of 
#  N contest codes. Each code is either START38 or LTIME108, to which each problem belongs.
# Output Format
# For each test case, output two integers in a single new line - the first integer
# should be the number of problems in START38, and the second integer should be the 
# number of problems in LTIME108.
c = []
for i in range(int(input())):
    d = []
    s,l=0,0
    a = int(input())
    b = list(input().split())
    for i in b:
        if i.lower() == 'start38':
            s +=1
        else:
            l+=1
    d.append(s)
    d.append(l)
    c.append(d)
for i in c:
    print(i[0], i[1])






