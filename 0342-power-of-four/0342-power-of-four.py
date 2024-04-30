class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True
        elif n < 1:
            return False
        elif n%4 != 0:
            return False

        return self.isPowerOfFour(n//4)
        