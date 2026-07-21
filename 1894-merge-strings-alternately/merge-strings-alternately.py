'''
Tentukan variabel dan nilai result berupa array kosong
Iterate using while for both word
While iterate do append for both word
Cek salah satu dari sisa append dan tambahkan
Join result to make a string as expected
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = word1, word2
        i, j = 0, 0

        res = []

        for i in range (min(len(w1), len(w2))):
            res.append(w1[i])
            res.append(w2[i])
            i += 1
        res.append(w1[i:])
        res.append(w2[i:])

        return "".join(res)