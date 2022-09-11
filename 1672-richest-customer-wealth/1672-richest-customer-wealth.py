#Each array contains the amount of cash stored in three banks by a single person. 

class Solution(object):        
    def maximumWealth(self, accounts: List[List[int]]) -> int:   
        maxWealth = 0   
        for i in range(len(accounts)):        
            totalWealth = sum(accounts[i])     
            maxWealth = max(maxWealth, totalWealth) 
        return maxWealth

#The process initially defines a value of maxWealth to equal 0. It then loops through all accounts using the for loop, and sums the amount within each account. It then compares the totalWealth with a stored maxWealth (initially 0, but each loop will be the highest value of totalWealth accumulated) and stores the highest value of maxWealth from all loops, and prints it out.

#LINE BREAKDOWN

#class Solution(object): - Creates a class in order to process the multple data points
    
#def maximumWealth(self, accounts: List[List[int]]) -> int: - Defines accounts as a list of a list of integer numbers, or in this case, a collection (list #1) of wealth stored (integer number) in multiple banks (list #2)
        
#maxWealth = 0 - Creates a variable called "maxWealth"
        
#for i in range(len(accounts)): - This will loop through the length of each account, for every account avaiable
            
#totalWealth = sum(accounts[i]) - This defines the variable "totalWealth" as the sum of the individual accounts throughout the multiple banks
            
#maxWealth = max(maxWealth, totalWealth) - This will compare the maximum wealth we set as a variable (0) with the total wealth calculated for this array. It then stores maxWealth as the total wealth for that loop. Everytime it loops, it will check to see if the new totalWealth in the other array is greater than the one stored. If so, it stores a new maxWealth, if not, it discards. Returns the highest maxWealth after all loops
    
#return maxWealth - Prints out value of maxWealth
        



        