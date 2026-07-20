class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = len(str1)
        j = len(str2)

        minimumValue = min(i, j)

        def isDivisor(l):
            if i % l or j % l:
                return False
            factor1, factor2 = i // l, j // l
            return str1[:l] * factor1 == str1 and str1[:l] * factor2 == str2

        for l in range(minimumValue, 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""