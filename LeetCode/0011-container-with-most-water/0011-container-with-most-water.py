class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        s, e = 0, len(height)-1

        # go to more big one
        while s < e :
            tmp = min(height[s], height[e]) * (e-s)
            if (height[s] < height[e]) :
                s += 1
            elif (height[s] > height[e]) :
                e -= 1
            elif (height[s] == height[e]) :
                s += 1
                e -= 1
            print(s, e)
            ans = max(ans, tmp)

        return ans