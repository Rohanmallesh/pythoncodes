# Problem
# Chef categorises an instagram account as spam, if, the following count of the account is more than 10 times the count of followers.

# Given the following and follower count of an account as X and  Y respectively, find whether it is a spam account.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two space-separated integers X and  Y — the following and follower count of an account, respectively.

# x = int(input('enter x value'))
# y = int(input('enter y value'))

def chechspam(x,y):
    if x/y > 10:
        print('YES')
    else:
        print('NO')
for t in range(int(input())):
    x,y = map(int ,input('input together').split())
    chechspam(x,y)







