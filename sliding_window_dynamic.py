"""
A generic template for dynamic sliding window finding min window length
"""
def shortest_window(nums, condition):
    i = 0
    min_length = float('inf')
    result = None

    for j in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Shrink window as long as the condition is met
        while condition():  
            # Update the result if the current window is smaller
            if j - i + 1 < min_length:
                min_length = j - i + 1
                # Add business logic to update result

            # Shrink the window from the left
            # Remove nums[i] from the current window logic
            i += 1

    return result


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

    window_chars = set()

    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in window_chars:
            window_chars.remove(s[left])
            left += 1

        window_chars.add(s[right])
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


s1 = "abcabcbb"
print(f"String: '{s1}'")
print(f"Max Length: {length_of_longest_substring(s1)}") # Output: 3 ("abc")