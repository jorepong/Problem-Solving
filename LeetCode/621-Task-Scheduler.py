class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = {}
        for task in tasks:
            task_map[task] = 1 + task_map.get(task, 0)

        heap = []

        for task in set(tasks):
            heapq.heappush(heap, -task_map[task])

        queue = deque()
        clock = 0
        while heap or queue:
            clock += 1
            
            if heap:
                item = heapq.heappop(heap)
                if item + 1 != 0:
                    queue.append((item+1, clock+n))
            
            if queue and queue[0][1] == clock:
                item = queue.popleft()
                heapq.heappush(heap, item[0])
        
        return clock