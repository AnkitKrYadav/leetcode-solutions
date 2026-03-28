class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,mfreq=0,0
        freq,best={},1
        for j in range (len(s)):
            freq[s[j]] = freq.get(s[j],0)+1
            mfreq = max(mfreq,freq[s[j]])

            if(j-i+1-mfreq > k):
                freq[s[i]]-=1;
                i+=1
            else:
                best = max(best,(j-i+1))
        return best
#O(n),O(1)
        