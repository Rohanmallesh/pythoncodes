# # iven the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# # Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# # Example

# # The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.
lis =[]
for i in range(int(input())):
    lis1 = [None]*2
    n = input()
    m = float(input())
    lis1[0]=n
    lis1[1]=m
    lis.append(lis1)
lis.sort()
print(lis)
st = set()
for i in lis:
    st.add(i[1])
rev =[]
for i in st:
    rev.append(i)
rank =[]
for i in range(1,len(lis)):
    if lis[i][1] == rev[1]:
        rank.append(lis[i])

for i in rank:
   print(i[0])