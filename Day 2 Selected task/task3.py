"""
3. https://codeforces.com/problemset/problem/1793/B
"""

lmx = 5
lmi = -3
list_1 = []
list_2 = []

for i in range(lmx-lmi):
    # print(lmx)
    list_1.append(lmx)
    lmx -= 1
    list_2.append(lmi)
    lmi += 1

print(len(list_1+list_2))
print(list_1 + list_2)

