class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
#main idea is to have key values in map as sorted words from strs and 
#values as words which are anagram to key itself
#.setdefalut is used to enter key and value to a map
        for i in strs:
            m.setdefault(''.join(sorted(i)),[]).append(i)
        
        return m.values()
         
