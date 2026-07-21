class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        shortestLength = min(len1, len2)

        # isDivisor ngecek modulo dan faktor
        def isDivisor(i):
            if len1 % i or len2 % i:
                return False
            factor1, factor2 = len1 // i, len2 // i
            subset = str1[:i]
            return subset * factor1 == str1 and subset * factor2 == str2

        for i in range(shortestLength, 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""