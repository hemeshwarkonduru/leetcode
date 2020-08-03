class Solution:
    #using dynamicprogramming matrix table
    def longestPalindrome(self, s: str) -> str:
        d=[[0 for i in range(len(s))]for j in range(len(s))]
        l1=1
        strt=0
        #we first have to fill the table for lengths 1 and 2
        for i in range(len(s)):
            d[i][i] = 1
            i+=1
            
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                strt=i
                l1=2
                d[i][i+1]=1
            
        
        i=0
        k=3
        while(k<=len(s)):
            i=0
            while(i<=len(s)-k):
                j=i+k-1
                if(s[i]==s[j] and d[i+1][j-1]==1):#condition to check the previous palindromic string
                    d[i][j]=1
                    if(k>l1):
                        l1=k
                        strt=i
                i+=1
            k+=1
        return s[strt:strt+l1]
#refer youtube video for better understanding