class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        w2s = []
        for i,m in enumerate(mat):
            strength = (sum(m), i)
            w2s.append(strength)
            
        w2s.sort()
        return [i[1] for i in w2s[:k]]

           
        