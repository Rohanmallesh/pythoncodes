# You are moving to a new city and have a big decision to make.
# You can lease an apartment at 
# A dollars per year OR
# You can purchase the apartment at
# B dollars.
# Assume you are in a zero interest rate country - for how many years 
# will the total cost of leasing the apartment be lesser than the cost of outright purchase?

# Input Format
# The first line of input will contain an integer 
# T — the number of test cases. The description of 
# T test cases follows.
# The first and only line of each test case contains two integers 
# A and B
# Output Format
# For each test case, output the maximum number of years where the total cost of
# leasing the apartment is lesser than the cost of outright purchase

for i in range(int(input())):
    a,b = map(int,input().split())
    
    k = b//a
    print(k)


