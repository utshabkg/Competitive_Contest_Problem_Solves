class Solution:
    def minPartitions(self, n: str) -> int:
        numbers = []

        for i in n:
            numbers.append(int(i))

        return max(numbers)