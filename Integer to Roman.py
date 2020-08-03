class Solution:
    def intToRoman(self, num: int) -> str:
        dixt={1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}
        
        roman=""
#checks all the dictionary values one by one in increasing order
        for i in dixt.keys():
            roman=roman+dixt[i]*(num//i)#num//i returns 0 or 1 when one by one value
            #from dictionary is taken from increasing value
            num%=i
            #remainder after the conversion
            

        
        return roman