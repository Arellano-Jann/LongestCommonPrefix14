class Solution(object):
    def longestCommonPrefix(self, strs):
        common = ""
        strs.sort(key = lambda x: len(x))
        print(strs)
        if len(strs) == 1:
            return "".join(strs)
        for word1 in strs[1:]:
            print(word1, "word1")
            word2 = strs[0]
            for char in range(len(word2)):
                if word1[char] == word2[char]:
                    common += word1[char]
                else:
                    break
            common += " "
        commonList = common.split()
        print(commonList)
        if len(commonList) > 1:
            return self.longestCommonPrefix(commonList)
        return "".join(commonList)
                
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["cir","car"]))
print(Solution().longestCommonPrefix(["a"]))
