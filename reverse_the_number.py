# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, display the reverse of the given number N, in a new line.

for i in range(int(input())):
    t = input()
    ans = ''
    for i in str(t):
        ans = i + ans
    print(int(ans))


