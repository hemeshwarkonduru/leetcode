class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m={}
        maxi=0
        i=j=0 #here j variable crucial for sliding
        while i<len(s):
            if(s[i] in m and j<=m[s[i]]):#the condition j<=m[s[i]] is crucial, check for s="tmmzuxt"
#as j value goes to 1 when second t is encountered
                j=m[s[i]]+1
            else:
                maxi = max(maxi,i-j+1)
            m[s[i]]=i
            i+=1
            
        
        return maxi
    