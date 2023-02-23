import array as ary
a = ary.array('i',[])
c = int(input())
b = list(map(int,input().split()))
for i in b:
    a.append(i)
a.reverse()
for i in a:
   print(i , end=" ")