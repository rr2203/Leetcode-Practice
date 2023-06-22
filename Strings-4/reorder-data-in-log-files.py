# TC: O(nlogn) | SC: O(1)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def comparator (log):
            identifier, content = log.split(' ', 1)

            if content[0].isalpha():
                return (0, content, identifier)
            else:
                return (1,)

        logs.sort(key=comparator)
        return logs