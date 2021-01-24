"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water_volume = 0
        max_left_wall = height[0]
        max_right_wall = height[-1]
        # Two - Pointer
        left, right = 0, len(height)-1

        while left < right:
            max_left_wall = max(max_left_wall, height[left])
            max_right_wall = max(max_right_wall, height[right])

            if max_left_wall < max_right_wall:
                water_volume += max_left_wall - height[left]
                left += 1

            else:
                water_volume += max_right_wall - height[right]
                right -= 1
        return water_volume

