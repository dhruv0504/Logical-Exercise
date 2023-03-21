"""
10. https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff5/0000000000051185
"""

all_arrangement = [[0,0,0,0], [0,0,0,1],[0,0,1,0],[0,0,1,1], [0,1,0,0], [0,1,0,1],[0,1,1,0], [0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]

forbidden_types = [[1,1,1,1],[0,1,1,1],[1,0,1,1],[1,1,0,1]]

choice = [[1,1,1,1],[1,1,1,1]]

com_buffer = []

for i in range(0,15):
    if all_arrangement[i] not in forbidden_types:
        count = 0
        for j in range(len(choice)):
            for k in range(4):
                if choice[j][k] != all_arrangement[i][k]:
                    count+=1
        com_buffer.append(count)

print(min(com_buffer))