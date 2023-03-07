"""
link: https://leetcode.com/problems/relative-ranks/
status: submitted

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

"""

score = [10,3,8,9,4]

def findRelativeRanks(score):
    ans=[]
    temp=sorted(score,reverse=True)
    for i in score:
        if(temp.index(i)==0):
            ans.append("Gold Medal")
            print(ans)
        elif(temp.index(i)==1):
            ans.append("Silver Medal")
            print(ans)
        elif(temp.index(i)==2):
            ans.append("Bronze Medal")
            print(ans)
        else:
            ans.append(str(temp.index(i)+1))
            print(ans)
    # return ans

print(findRelativeRanks(score))