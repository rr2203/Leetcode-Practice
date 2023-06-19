# TC: O(n) | SC: O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        allSubStrings = set()
        result = set()

        for i in range(len(s) - 9):
            currentSubString = s[i:i + 10]
            if currentSubString in allSubStrings:
                result.add(currentSubString)
            allSubStrings.add(currentSubString)

        return list(result)