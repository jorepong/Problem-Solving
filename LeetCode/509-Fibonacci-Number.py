class Solution:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if n not in self.mem:
            self.mem[n] = self.fib(n-1) + self.fib(n-2)

        return self.mem[n]