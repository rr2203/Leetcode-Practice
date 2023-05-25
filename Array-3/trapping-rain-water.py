# TC: O(n) | SC: O(1)
# Two pointers
class Solution:
    def trap(self, height):
        left_max, right_max, water = 0, 0, 0
        i, j = 0, len(height) - 1

        while i < j:
            left_max, right_max = max(left_max, height[i]), max(right_max, height[j])

            if left_max < right_max:
                water += (left_max - height[i])
                i += 1
            else:
                water += (right_max - height[j])
                j -= 1

        return water
    
# TC: O(n) | SC: O(n)
# Monotonic Stack
class Solution:
    def trap(self, height):
        water, current = 0, 0
        st = []
        while current < len(height):
            while st and height[current] > height[st[-1]]:
                top = st[-1]
                st.pop()
                if not st:  break
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                water += distance * bounded_height
            st.append(current)
            current += 1
        return water