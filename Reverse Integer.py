class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):#to tackle negative integers
            x*=-1
            y=str(x)
            out= '-'+(y[::-1])#minus is added at last as string
        else:
         
            y=str(x)
            out= (y[::-1])#if zeros are present in the string
#when converted to int they vanish
            
        
        if((int(out)>2147483647) or (int(out)<-2147483648)):#leetcode criteria
            return 0
        
        else:
            return int(out)
        