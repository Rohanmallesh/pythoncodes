# Problem
# There is a group of N friends who wish to enroll in a course together. The course has a maximum capacity of 
# M students that can register for it. If there are 
# K other students who have already enrolled in the course, determine if it will still be possible for all the 
# N friends to do so or not.

# Input Format
# The first line contains a single integer 
# T - the number of test cases. Then the test cases follow.
# Each test case consists of a single line containing three integers N, M and 
# K - the size of the friend group, the capacity of the course and the number of students already registered for the course.

for i in range(int(input())):
    n,m,k = map(int,input().split())
    temp = m-k
    if temp<n:
        print('NO')
    else:
        print('YES')



