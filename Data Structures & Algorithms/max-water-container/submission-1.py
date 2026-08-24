class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        out = 0
        i = 0
        j = n-1
        while i < j:
            area = (j-i)*(min(heights[i],heights[j]))
            out = max(area,out)
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return out
