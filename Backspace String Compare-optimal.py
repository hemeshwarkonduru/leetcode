class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i=len(S)-1
        j=len(T)-1
        skip1=skip2=0
        while(i>-1 or j>-1):
            c=S[i] if i>=0 else ""
            c1=T[j] if j>=0 else ""
            if(c=='#'):
                skip1+=1
                i-=1
                continue
            if(c1=='#'):
                skip2+=1
                j-=1
                continue
            if(skip1>0):
                skip1-=1
                i-=1
                continue
            if(skip2>0):
                skip2-=1
                j-=1
                continue
            if(c!=c1):
                return False
            i-=1
            j-=1
        
        return (i<0 and j<0)
'''
debug the code properly this is called two pointer approach
skip variable is used to keep track of #
'''        
        


    
                

            
            



            
            
        