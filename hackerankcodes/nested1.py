# # iven the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# # Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# # Example

# # The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.
lis = []
for i in range(int(input())):
    lis1 = [None]*2
    n = input()
    m=float(input())
    lis1[0]=n
    lis1[1]=m
    lis.append(lis1)
# print(lis)
st = set()
for i in lis:
    st.add(i[1])
# print(st)
lis2 = []
for i in st:
    lis2.append(float(i))
lis2 = list(st)
r=[]
for i in lis2:
    r.append(i)
r.sort()
# print(r)
rank=[]
for i in lis:
    if i[1]==r[1]:
        rank.append(i[0])
# print(rank)
rank.sort()
for i in rank:
    print(i)