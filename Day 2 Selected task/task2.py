"""
2. https://codeforces.com/problemset/problem/1800/A

"""
str = "meowA"

l_string = str.lower()
list = [x for x in l_string]

res = []
for i in list:
    if i not in res:
        res.append(i)

if res == ['m', 'e', 'o', 'w']:
    print("YES")
else:
    print("NO")