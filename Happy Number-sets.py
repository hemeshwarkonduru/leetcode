class Solution:

    
    def isHappy(self, n: int) -> bool:
        s=set()
        
        while(True):
            if(n in s):
                return False
#a number is not happy number if its sum of squares repeat
            s.add(n)
            temp=n
            su=0
            while(temp!=0):
                su+=(temp%10)**2
                temp=temp//10
        
            if(su==1):
                return True
            n=su

            

            