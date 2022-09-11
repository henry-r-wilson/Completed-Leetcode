class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        w2s = []
        for i,m in enumerate(mat):
            strength = (sum(m), i)
            w2s.append(strength)
            
        w2s.sort()
        return [i[1] for i in w2s[:k]]

#Makes a list for final answer, calling it w2s (weakest to strongest). We then make a for loop, in which we assign the row (i) and the value within the row (m), and then use the "enumerate" function, which then labels the row as a integer number going upwards from 0. We then say that the strength of the row is the sum of the values within the row, and assign the row number to it. We then place the list of strengths into the w2s list made earlier. From here, we sort the strength from lowest to highest. Finally, we print out the list of row strength, but change it so that it prints out the row number for i in the w2s row k.

#LINE BREAKDOWN
        
#w2s = [] - makes list to use later
        
#for i,m in enumerate(mat): - This assings the row (i) and the values with the row (m) within the enumerated matrix 'mat'. This enumerated matrix means the rows are now labelled from 0 to the maximum row number. 
            
#strength = (sum(m), i) - This assigns the strength to be equal to the sum of the binary value within each row i
            
#w2s.append(strength) - This appends that strength into the list made earlier
            
#w2s.sort() - This sorts that list into weakest to strongest
        
#return [i[1] for i in w2s[:k]] - This returns the sorted list of strength from lowest to highest. The changes made makes sure the row number is printed, rather than the values within each row.            
        