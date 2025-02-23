class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = {}
        for task in tasks:
            task_map[task] = 1 + task_map.get(task, 0)

        heap = []

        for task in set(tasks):
            heapq.heappush(heap, [0, -task_map[task], task])

        result = []
        clock = 0
        while heap:
            if heap[0][0] < clock:
                item = heapq.heappop(heap)
                task = item[2]
                heapq.heappush(heap, [clock, -task_map[task], task])
                continue
            elif heap[0][0] == clock:
                item = heapq.heappop(heap)
                task = item[2]

                result.append(task)
                task_map[task] -= 1

                if task_map[task] > 0:
                    heapq.heappush(heap, [clock + n + 1, -task_map[task], task])
            else:
                result.append('idle')
            clock += 1
        
        print(result)
        return len(result)