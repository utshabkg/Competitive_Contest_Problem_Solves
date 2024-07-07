class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        final = 0
        for i in range(len(operations)):
            current = operations[i]
            if "+" in current:
                final += 1
            else:
                final -= 1

        return final