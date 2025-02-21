class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
        
        context_map = {}
        have = 0
        need = len(t_map)
        start = 0
        res_len = float('inf')
        res = [-1, -1]
        for i in range(len(s)):
            c = s[i]
            context_map[c] = 1 + context_map.get(c, 0)

            if c in t and context_map[c] == t_map[c]:
                have += 1

            while have == need:
                if (i - start + 1) < res_len:
                    res_len = i - start + 1
                    res = [start, i]
                context_map[s[start]] -= 1
                if s[start] in t and context_map[s[start]] < t_map[s[start]]:
                    have -= 1
                start += 1

        l, r = res[0], res[1]
        return s[l:r+1] if res_len != float('inf') else ''
