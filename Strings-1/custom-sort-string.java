/*
 * 
 * TC: O(n)
 * SC: O(n) (Coz we used string builder)
 * 
 */

class Solution {
    public String customSortString(String order, String s) {
        char[] sFreq = new char[26];
        for(int i=0; i<s.length(); i++)   {
            sFreq[s.charAt(i)-'a']++;
        }

        StringBuilder ans  = new StringBuilder();
        for(int i=0; i<order.length(); i++)   {
            for(int j=0; j<sFreq[order.charAt(i)-'a']; j++) {
                ans.append(order.charAt(i));
            }
            sFreq[order.charAt(i)-'a'] = 0;
        }
        for(int i=0; i<26; i++) {
            for(int j=0; j<sFreq[i]; j++)
                ans.append((char)('a'+i));
        }

        return ans.toString();
    }
}