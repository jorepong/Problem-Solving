class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = collections.defaultdict(int)
        heap = [(0, k)]
        visited = set()

        while heap:
            w, v = heapq.heappop(heap)

            if v in visited:
                continue

            dist[v] = w
            visited.add(v)

            for inner_v, inner_w in graph[v]:
                if inner_v not in visited:
                    heapq.heappush(heap, (inner_w + w, inner_v))

        result = max(dist.values())

        return result if len(dist) == n else -1