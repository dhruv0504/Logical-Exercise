"""
4.  https://www.codechef.com/problems/ATM2
"""
t_c = int(input("Enter no. of test cases:"))

for i in range(t_c):
    ar = input()
    ar_li = ar.split(" ")
    
    n_p = int(ar_li[0])
    t_amnt = int(ar_li[1])
    trans = input()
    f_trans = trans.split(" ")
    # print(f_trans)

    ans = ""
    for j in range(n_p):
        if int(f_trans[j]) <= t_amnt:
            ans += "1"
            t_amnt -= int(f_trans[j])
        else:
            ans += "0"
    print(ans)
         
        
        