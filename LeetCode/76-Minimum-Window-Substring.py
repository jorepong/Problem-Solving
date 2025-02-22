class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = collections.Counter(t)

        need = len(t)

        left = 0
        min_len = float('inf')
        min_context = [-1, -1]
        for right in range(len(s)):
            c = s[right]

            need -= t_map[c] > 0
            t_map[c] -= 1

            if need == 0:
                while left < right and t_map[s[left]] < 0:
                    t_map[s[left]] += 1
                    left += 1
                
                if (right - left + 1) < min_len:
                    min_len = (right - left + 1)
                    min_context = [left, right]
                
                t_map[s[left]] += 1
                left += 1
                need += 1
        
        return s[min_context[0]:min_context[1]+1] if min_len != float('inf') else ''