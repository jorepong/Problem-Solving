class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        p1 = 0
        p2 = 0
        max_len = 0

        while not (len(set(s[p1:p2])) == p2 - p1 and len(s) == p2):
            if len(s) - p1 <= max_len:
                break

            if len(set(s[p1:p2])) != p2 - p1:
                p1 += 1
            else:
                max_len = max(max_len, p2 - p1)
                p2 += 1
        max_len = max(max_len, p2 - p1)

        return max_len        