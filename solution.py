class Solution(object):
    def longestCommonPrefix(self, strs):
        common = ""
        strs.sort(key = lambda x: len(x))
        for word1 in strs[1:]:
            word2 = strs[0]
            for char in range(len(word2)):
                if word1[char] == word2[char]:
                    common += word1[char]
            common += " "
        commonList = common.split()
        if len(commonList) == 1:
            return "".join(commonList)
        return self.longestCommonPrefix(commonList)
                
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
