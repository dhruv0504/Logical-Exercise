"""
9. https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed

"""
count_p = 0
count_m = 0
count = 0
flag_p = True
flag_m = True
N_p = N_m = 139



while flag_p == True:

    list_of_digits_plus = [int(i) for i in str(N_p)]
    list_of_digits_minus = [int(i) for i in str(N_m)]

    for i in list_of_digits_plus:
        N_b = N_p
        # print(N_b)
        if i%2 != 0:
            N_b += 1
            # print(N_b)
            count_p += 1    
            # print(count_p)
            break
    if N_b == N_p:
        flag_p = False
    else:
        N_p = N_b
    

    for i in list_of_digits_minus:
        N_b = N_m
        # print(N_b)
        if i%2 != 0:
            N_b -= 1
            # print(N_b)
            count_m += 1    
            # print(count_m)
            break
    if N_b == N_m:
        flag_p = False
    else:
        N_m = N_b
    
print(min(count_m,count_p))