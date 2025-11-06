from typing import List
"""
A generic template for dynamic sliding window finding min window length
"""
def shortest_window(nums, condition):
    left = 0
    min_length = float('inf')
    result = None

    for right in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Shrink window as long as the condition is met
        while condition():  
            # Update the result if the current window is smaller
            if right - left + 1 < min_length:
                min_length = right - left + 1
                # Add business logic to update result

            # Shrink the window from the left
            # Remove nums[i] from the current window logic
            left += 1

    return result

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            Find the minimum subarray with the given target sum.
            **Note**: Use dynamic window to solve this problem
            Consist of expanding the window and shrinking the window
        """
        import math

        if not target or not nums:
            return 0
        left = 0
        window_sum = 0

        min_length = math.inf 

        for right in range(len(nums)):
            # expand the window until we get to the target sum
            # usually on the right side
            window_sum += nums[right]

            # shrink the window to the smallest length
            # (usually on the left side)
            while window_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)

                window_sum -= nums[left]
                left += 1
        
        return 0 if min_length == math.inf else min_length


"""
A generic template for dynamic sliding window finding max window length
"""
def longest_window(nums, condition):
    i = 0
    max_length = 0
    result = None

    for j in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Shrink the window if the condition is violated
        while not condition():  
            # Shrink the window from the left
            # Remove nums[i] from the current window logic
            i += 1

        # Update the result if the current window is larger
        if j - i + 1 > max_length:
            max_length = j - i + 1
            # Add business logic to update result

    return result


def length_of_longest_substring(s: str) -> int:
    """
        Find the length of the longest substring without repeating characters
    """
    # use a set to check for duplicate
    window_chars = set()

    left = 0
    max_length = 0

    for right in range(len(s)):

        # shrink until there is no duplicate
        while s[right] in window_chars:
            window_chars.remove(s[left])
            left += 1
        
        # expand automatically to try to get the longest substring
        window_chars.add(s[right])
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length
