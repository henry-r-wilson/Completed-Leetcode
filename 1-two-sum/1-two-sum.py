class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        HashMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return[HashMap[diff], i]
            HashMap[n] = i
        return 
                
#This problem utilises HashMaps, which maps the value within a string or array into a index which can be consulted at O(n) time. What the code does is two things simultaneously. It will check a value, and then take away that value from the target number (e.g. target = 10 and current value = 2, it will give 8.) It will then check to see if 8 exists in the current HashMap. If not, it adds the current value to the HashMap and goes to the next value. This repeats until a value it is looking for is in the HashMap, in which case it provides the HashMaps index for the current value and the value it is looking for.   

#HashMap = {} - Creates a HashMap, also called a dictionary in Python

#for i, n in enumerate(nums): - For values in index (i) and values in array (n) which have been enumerated for easier access, do action.

#diff = target - n - Define the difference between the current number and the target number as 'diff'

#if diff in HashMap: - If a value for this difference is present in the HashMap, do action

#return[HashMap[diff], i] - Action is to return the current index value for the diff value in the HashMap, and the index value for the currently assessed value 

#HashMap[n] = i - If solution is not found, update the HashMap

#return - If no solution is found, return 
                
        