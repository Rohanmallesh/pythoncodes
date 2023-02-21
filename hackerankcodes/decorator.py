# Let's use decorators to build a name directory! You are given
# some information about  people. Each person has a first name,
# last name, age and sex. Print their names in a specific format 
# sorted by their age in ascending order i.e. the youngest person's 
# name should be printed first. For two people of the same age, 
# print them in the order of their input.

lis = []
for i in range(int(input())):
    line=[]
    f,l,a,s = map(str,input().split())
    line.append(f)
    line.append(l)
    line.append(int(a))
    line.append(s)
    lis.append(line)
s = set()
# print(s)
for i in lis:
    s.add(i[2])
r = list(s)
r.sort()
# print(r)
for i in r:
    for j in lis:
        if j[2]==i:
            if j[-1]== 'm' or 'M':
                print(f'Mr.{j[0]} {j[1]}')
            else:
                print(f'Ms.{j[0]} {j[1]}')
