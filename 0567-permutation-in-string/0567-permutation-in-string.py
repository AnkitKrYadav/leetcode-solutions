class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1,f2,i={},{},0
        if len(s2) < len(s1):
            return False
        for j in range(len(s1)) :
            f1[s1[j]] = f1.get(s1[j],0)+1
            f2[s2[j]] = f2.get(s2[j],0)+1

        if f1 == f2: return True
        else: j += 1

        while(j < len(s2)):
            f2[s2[i]] -= 1; 
            if f2[s2[i]] == 0:
                del f2[s2[i]]
            i += 1
            f2[s2[j]] = f2.get(s2[j],0)+1

            if f1 == f2:
                return True
            j+=1
        return False
        
#O(n^2),O(len(s2))
