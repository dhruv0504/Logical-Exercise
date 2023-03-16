"""
2. cgpt
Given an array of strings, group anagrams together.
Example: Input: ["eat", "tea", "tan", "ate", "nat", "bat"]. Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""
def groupAnagrams(strs):
    
    dict = {}

    for word in strs:
        s_word = "".join(sorted(word))

        if s_word not in dict:
            dict[s_word] = [word]

        else:
            dict[s_word].append(word)

    result =[]
    for item in dict.values():
        result.append(item)
    
    return result


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))