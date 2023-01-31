
p1,p2,p3,p4 = map(int,input().split())
count=0
k = [p1,p2,p3,p4]
for i in k:
    if i>=10:
        count += 1
print(count)
