class Solution(object):
    def findValidPair(self, s):
        from collections import Counter
        counts = Counter(s)
        for i in range(len(s) - 1):
            first, second = s[i], s[i + 1]
            if first != second and counts[first] == int(first) and counts[second] == int(second):
                return first + second
        return ""