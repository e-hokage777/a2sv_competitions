class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ## case where only 1 string in list
        if len(strs) <= 1:
            return strs[0]
        elif len(strs[0]) == 0:
            return ""
        
        index = 0
        end = False
        for char in strs[0]:
            for i in range(1, len(strs)):
                if len(strs[i])== 0:
                    end = True
                    index = 0
                    break
                elif len(strs[i])-1 <  index or strs[i][index] != char:
                    print("char",char)
                    end = True
                    break

            index += 1

            if end: break

        return strs[0][:index-1]

solution = Solution()

inputs = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
    ["me", "mine"],
    ["work"],
    ["work", ""],
    ["",""],
    ["", "fan"],
    ["ab", "a"],
    ["a", "ab"]
]

if __name__ == "__main__":
    for _input in inputs:
        print(solution.longestCommonPrefix(_input))
        