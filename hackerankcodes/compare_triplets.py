# Alice and Bob each created one problem for HackerRank. A reviewer
# rates the two challenges, awarding points on a scale from 1 to 100
# for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]),
# and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing a[0] with 
# b[0], a[1] with b[1], and a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.

# Given a and b, determine their respective comparison points.

def compare_the_triplets( c,d):
    a ,b =0,0
    for i in range(0,len(c)):
        if c[i] != d[i]:
            if c[i]>d[i]:
                a += 1
            else:
                b+=1
        else:
            None
    return a,b
    
    
    
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if __name__ == '__main__':
    r ,t =compare_the_triplets(a,b)
    print(r , t)
    

