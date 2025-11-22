"""
A generic template for sliding window of fixed size
"""
def window_fixed_size(nums, k):
    left = 0
    result = None

    for right in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Ensure window has size of K
        if (right - left + 1) < k:
            continue

        # Update Result
        # Remove nums[i] from window
        # increment i to maintain fixed window size of length k
        left += 1

    return result

def window_fixed_size2(nums, k):
    """
    Could start looping at k if it is fixed
    """
    left = 0
    #base case
    max_sum = sum(nums[:k])
    window_sum = max_sum


    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[left]
        max_sum = max(max_sum, window_sum)
        left += 1

    return max_sum


# find max sum in a contiguous sub array of size k
def find_max_sum_sub_array(arr, k):
    if not arr or k == 0 or k > len(arr):
        return 0
    
    
    window_sum = sum(arr[:k]) # initialize the initial window
    max_sum = window_sum 
    left = 0

    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[left]
        max_sum = max(max_sum, window_sum)
        left += 1

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Array: {arr}")
print(f"Window size (k): {k}")
print(f"Maximum Sum: {find_max_sum_sub_array(arr, k)}")