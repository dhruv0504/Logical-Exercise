"""
7. https://practice.geeksforgeeks.org/problems/check-frequencies4211/1?page=3&category[]=Hash&sortBy=submissions

"""
s = "xxxxyyzz"

def sameFreq(s):
    d={}
    for i in s:
        if( i not in d):d[i]=1
        else:
            d[i]+=1

    l1=list(d.values())
    l2=l1
    # print(l1)

    # for "CCCCCCC"

    if(l1.count(l1[0])==len(l1)):
        return True
    
    # for other string

    for i in range(len(l1)):
        
        if(l1.count(l1[i])==1):
            l2[i]-=1
            if(l2[i]==0):
                l2.remove(l2[i])
            break

    if(l2.count(l2[0])==len(l2)):
        return True
    
    else:
        return False

print(sameFreq(s))