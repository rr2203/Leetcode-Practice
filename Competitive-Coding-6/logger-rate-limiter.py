# Time efficient (Faster reponses but no memory cleanup of expired messages)
#TC: O(1)
#SC: O(# of unique messages)
from collections import defaultdict
class Logger:
    def __init__(self):
        self.messageTimestampMap = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        canPrint = False
        if timestamp - self.messageTimestampMap.get(message, -11) >= 10: 
            canPrint = True
            self.messageTimestampMap[message] = timestamp
        return canPrint

# Space Efficient (Slower responses but cleanup of expired messages)
#TC: O(expired messages before current timestamp)
#SC: O(1)
class Logger:

    def __init__(self):
        self.q = OrderedDict()  

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        #cleanup
        while self.q and list(self.q.values())[0] + 10 <= timestamp:
            print(list(self.q.values())[0])
            self.q.popitem(last = False)
            
        shdPrint = False
        if message not in self.q or self.q[message]-timestamp >= 10:
            self.q[message] = timestamp
            shdPrint = True
        return shdPrint