"""
8. google code jam (h)
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

"""
T = int(input("Enter no of test cases:"))

for k in range(T):

    R = int(input("Enter no of rows:"))
    C = int(input("Enter no of cols:"))

    for i in range(R):
        str1 = ""
        str2 = ""
        str3 = "+"
        for j in range(C):  
            if i == 0 and j == 0:
                str1 += "..+"
                str2 += "..|"
            elif i >=1 and j == 0:
                str1 += "+-+"
                str2 += "|.|"
            elif j == C-1:
                str1 += "-+"
                str2 += ".|"
            else:
                str1 += "-+"
                str2 += ".|"
        print(str1)
        print(str2)
        if i == R-1:
            for i in range(C):
                str3 += "-+"
            print(str3) 