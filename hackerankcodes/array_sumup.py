import array as ary
a = ary.array('i',[])
b = int(input())
c = list(map(int, input().split()))
for i in c:
    a.append(i)
s=0
for i in a:
    s += i
print(s)