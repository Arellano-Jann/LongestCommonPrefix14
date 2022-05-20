class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key = lambda x: len(x))
        common = ""
        for index, char in enumerate(strs[0]):
            for word in strs:
                if word[index] != char:
                    return common
            common += char
        return common

                
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print("Expected result: fl")
print()
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print("Expected result: ")
print()
print(Solution().longestCommonPrefix(["cir","car"]))
print("Expected result: c")
print()
print(Solution().longestCommonPrefix(["a"]))
print("Expected result: a")
print()
print(Solution().longestCommonPrefix(["reflower","flow","flight"]))
print("Expected result: ")
print()
