no_j = 0
m1 = 0
m2 = 0
t1 = 5
t2 = 0
t3 = 0
t2_b = 0
t3_b = 0
t4 = 0

while(m1 > -1 and m2 > -1 and t1>0 and t2>0 and t3>0 and t4>0):
    while(t1>0):
        m1 += 1
        m2 +=1
        t1 -=1
        no_j += 1
        print(m1)
        print(m2)
        print(no_j)
    while(m1>0):
        m1-=1
        m2+=1
        t2-=1
        no_j +=1
    while(m2>0):
        m2-=1
        m1+=1
        t3-=1
        no_j +=1

print(no_j)