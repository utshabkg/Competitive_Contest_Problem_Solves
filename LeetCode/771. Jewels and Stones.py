class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for i in jewels:
            result += stones.count(i)

        return result