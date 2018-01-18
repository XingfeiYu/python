class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        start = maxLength = 0
        hasChars = {}
        for i in range(len(s)):
            if s[i] in hasChars and start <= hasChars[s[i]]: start = hasChars[s[i]] + 1
            else: maxLength = max(maxLength, i - start + 1)
            hasChars[s[i]] = i
        return maxLength

s = Solution()
print s.lengthOfLongestSubstring("aab")