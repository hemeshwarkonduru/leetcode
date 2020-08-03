class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=""
        if(len(strs)==0):
            return ""
        mini=65644645
        for i in range(len(strs)):
            mini=min(mini,len(strs[i]))
        
        
        k=""
        flag1=True
        for i in range(mini):
            flag1=True
            k=strs[0][i]
            for j in range(len(strs)):
                if(k!=strs[j][i]):
                    flag1=False
                    break
            if(not flag1):
                break
            else:
                out+=k
        return out
                

'''
flag plays a keen role as for test case
["aba","cca"] the out should be ""
so if any disruption in sequential characters break the loop

                    

                    

            
 
            
            
            
            
        
        
        
        