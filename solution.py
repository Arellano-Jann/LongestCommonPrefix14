class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key = lambda x: len(x))
        print(strs)
        common = ""
        for charIndex in range(1, len(strs[0])):
            for word in strs[1:]:
                if word.startswith(strs[0][0:charIndex]):
                    print(word, "startswith", strs[0][0:charIndex])
                    common += strs[0][charIndex-1]
                else:
                    break
        if len(strs) == 1:
            return "".join(strs)
        common = "".join(dict.fromkeys(common))
        for x in strs:
            if x.startswith(common):
                continue
            else:
                return ""
                
                
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
