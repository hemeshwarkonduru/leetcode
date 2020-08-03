#this code is like finding lengths till a dupliacte comes
#if a duplicate has come remove the character till that place using j

def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        max1=0
        j=i=0
        while(i<len(s)):
            if(s[i] in s1):
                s1.remove(s[j])
                j+=1
            else:
                s1.add(s[i])
                i+=1
                max1=max(max1,i-j)
        
        return max1
                