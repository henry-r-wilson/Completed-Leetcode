class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False

#This code logs the numbers into a new set, and then checks to see if the numbers repeat themselves witin that set.

#num_set = set() - Creates a set in which the numbers can be logged and then checked

#for i in nums: - States to check for all numbers in the list

#if i in num_set: - States that if a number i is found inside the number set, do action

#return True - Action is to return value as true
            
#num_set.add(i) - Adds the next number into the subset to be checked
        
#return False - If no values duplicate, return False
    

                
        