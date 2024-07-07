class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for i in sentences:
            max_words = max(max_words, i.count(" "))

        return max_words + 1