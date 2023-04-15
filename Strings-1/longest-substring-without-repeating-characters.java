/*
 * 
 * TC: O(n)
 * SC: O(1)
 * 
 */
import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastOccurence = new HashMap<>();
        int maxLen = 0;
        int windowStart = 0;

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(lastOccurence.containsKey(c))    {
                windowStart = Math.max(windowStart, lastOccurence.get(c)+1);
            }
            lastOccurence.put(c, i);
            maxLen = Math.max(maxLen, i-windowStart+1);
        }

        return maxLen;
    }
}