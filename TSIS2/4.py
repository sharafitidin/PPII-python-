class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0 
        maxi = 0
        for i in gain:
            ans += i
            if ans > maxi:
                maxi = ans
        return maxi