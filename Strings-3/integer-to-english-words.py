"""
TC: O(1)
SC: O(1)
"""
class Solution:
    below20 = [
        "Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
        "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"
    ]
    tens = [
        "","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety",
    ]
    suffixes = [
        "","Thousand","Million","Billion"
    ]

    def helper(self, num) -> str:
        if num==0: return ""

        if num<20:
            return self.below20[num] + " "
        elif num<100:
            return self.tens[num//10] + " " + self.helper(num%10)
        else:
            return self.below20[num//100] + " Hundred " + self.helper(num%100)
            

    def numberToWords(self, num: int) -> str:
        if num == 0: return self.below20[num]
        
        result = ""
        i=0
        while num:
            if num%1000 : result = self.helper(num%1000) + self.suffixes[i] + " " + result 
            num//=1000
            i+=1
        return result.strip()

