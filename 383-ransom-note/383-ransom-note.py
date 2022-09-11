class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        
        if len(ransomNote) > len(magazine):
            return False
        
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            elif ran[ransomNote[i]] > mag[ransomNote[i]]:
                return False 
        return True

#This code initially counts the amount of letters in each list (e.g if aab, output will be a = 2, b = 1). It then says that if the length of the ransomNote is greater than the length of the magazine, return a False (If there are more letters in the ransomNote than in the magazine, the ransomNote can't be made, since there isn't enough in the magazine to make the ransomNote). From here, we say that for the letters in the list ransomNote, if a single letter in ransomNote is not available in magazine, return a False (Can't make a ransomNote from letters not present). Then we say that if the amount of a specific letter 'i' in ransomNote is greater than the amount of specific letters 'i' in magazine, return a False (can't use more letters than are available). Finally, is all of these statements aren't true, return a True. This process focuses on what isn't there, rather than what is. 

#ran = Counter(ransomNote) - Counts the integer number of letters in list 'ransomNote'

#mag = Counter(magazine) - Counts the integer number of letters in list 'magazine'
        
#if len(ransomNote) > len(magazine): - States that if the length of list 'ransomNote' is greater than the list 'magazine', do action
            
#return False - Action is to return output as 'False'
        
#for i in range(len(ransomNote)): - This will loop through the length of each ransomNote list given
            
#if ransomNote[i] not in magazine: - This states that if a letter in ransomNote is not in magazine, do action
                
#return False - Action is to return output as 'False' 
            
#elif ran[ransomNote[i]] > mag[ransomNote[i]]: - This states that if the amount of a certain letter in ransomNote is greater than the amount of certain letter in magazine, do action
                
#return False - Action is to return output as 'False'
        
#return True - If all prior statements are false, return output as 'True'
            
     