class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(i):
            if len1 % i or len2 % i:
                return False
            factor1, factor2 = len1 // i, len2 // i
            return str1 == factor1 * str1[:i] and str2 == factor2 * str1[:i]

        for i in range(min(len1, len2), 0, -1):
            if isDivisor(i):
                return(str1[:i])

        return ""