class Solution:
    def romanToInt(self, s: str) -> int:
        value=0
        m={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        prev=0
        #prev holds previous value in the dictionary
        for i in range(len(s)):
            if(m[s[i]] > prev):
                value+=m[s[i]]-2*prev
                
            else:
                value+=m[s[i]]
            prev=m[s[i]]
        
        return value


