class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].lower() not in "abcdefghijklmnopqrstuvwxyz":
                left += 1
            elif s[right].lower() not in "abcdefghijklmnopqrstuvwxyz":
                right -= 1
            elif s[right].lower() != s[left].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

            
            
            
            
        