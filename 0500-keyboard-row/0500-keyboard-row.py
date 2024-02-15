class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        key_row_map = {
            "q":1,
            "w":1,
            "e":1,
            "r":1,
            "t":1,
            "y":1,
            "u":1,
            "i":1,
            "o":1,
            "p":1,
            "a":2,
            "s":2,
            "d":2,
            "f":2,
            "g":2,
            "h":2,
            "j":2,
            "k":2,
            "l":2,
            "z":3,
            "x":3,
            "c":3,
            "v":3,
            "b":3,
            "n":3,
            "m":3,
        }

        result =  []


        for word in words:
            belongs = True
            row = key_row_map[word[0].lower()]
            for letter in word:
                if key_row_map[letter.lower()] != row:
                    belongs = False
                    break
            if belongs:
                result.append(word)

        return result

        