# The provided code stub will read in a dictionary containing 
# key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name
# provided, showing 2 places after the decimal.
# Input Format

# The first line contains the integer n , the number of students'
# records. The next n lines contain the names and marks obtained by
# a student, each value separated by a space. The final line contains 
# query_name, the name of a student to query.
dist = {}
for i in range(int(input())):
    n,a,b,c = map(str,input().split())
    dist[n]=[float(a),float(b),float(c)]
print(dist)
s = input()
k = dist[s]
a=0
for i in k:
    a += i
avg = a/len(k)
print(f'{avg:.2f}')    


