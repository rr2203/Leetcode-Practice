/*
 * 
 * TC: O(m+n)
 * SC: O(1)
 * 
 */
import java.util.*;
class Solution {
    public List<Integer> findAnagrams(String s, String p) {

        List<Integer> ans = new ArrayList<>();
        if(s.length()<p.length()) return ans;


        Map<Character, Integer> pFreq = new HashMap<>();
        for(int i=0; i<p.length(); i++)
            pFreq.put(p.charAt(i), pFreq.getOrDefault(p.charAt(i), 0) + 1);

        int matched = 0;
        for(int i=0; i<s.length(); i++) {
            char incoming = s.charAt(i);
            if(pFreq.containsKey(incoming)) {
                int count = pFreq.get(incoming);
                count--;
                if(count == 0)  matched++;
                pFreq.put(incoming, count);
            }
            
            if(i>=p.length())   {
                char outgoing = s.charAt(i - p.length());
                if(pFreq.containsKey(outgoing)) {
                    int count = pFreq.get(outgoing);
                    count++;
                    if(count==1)    matched--;
                    pFreq.put(outgoing, count);
                }
            }

            if(matched == pFreq.size()) {
                ans.add(i-p.length()+1);
            }
        }

        return ans;

    }
}