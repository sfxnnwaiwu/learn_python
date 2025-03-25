
import string

'''
Sliding Window Technique
Concept
The Sliding Window technique is used to optimize problems involving subarrays or substrings where you need to analyze or compute 
a result over a contiguous segment of an array or string.

When to Use:

When dealing with contiguous subarrays/substrings.
Problems involving sums, maximum/minimum values, or unique elements.
Key Idea: Instead of recalculating the result for every subarray from scratch, maintain a "window" that slides across the array. 
Update the result by adding the incoming element and removing the outgoing element.
'''

# 1. Maximum Sum of a Subarray of Size K
# Problem: Find the maximum sum of any subarray of size k.


def max_subarray_sum_k(nums, k):
    max_sum = 0
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]  # Add the next element

        # Shrink the window if it exceeds size k
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            # Remove the element going out of the window
            window_sum -= nums[start]
            start += 1  # Slide the window forward

    return max_sum


# Example:
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_subarray_sum_k(nums, k))  # Output: 9 (subarray [5, 1, 3])

# =================================================================================

# 2. Longest Substring Without Repeating Characters
# Problem: Find the length of the longest substring without repeating characters.


def longest_unique_substring(s):
    char_index = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1  # Slide the window

        char_index[s[end]] = end  # Update the character's index
        max_length = max(max_length, end - start + 1)

    return max_length


# Example:
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3 (substring "abc")

# ====================================================================================

# 3. Smallest Subarray with a Given Sum
# Problem: Find the smallest subarray with a sum >= target.


def smallest_subarray_with_sum(nums, target):
    min_length = float('inf')
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        # Shrink the window until the sum is smaller than target
        while window_sum >= target:
            min_length = min(min_length, end - start + 1)
            window_sum -= nums[start]
            start += 1

    return min_length if min_length != float('inf') else 0


# Example:
nums = [4, 2, 2, 7, 8, 1, 2, 8, 1, 0]
target = 8
print(smallest_subarray_with_sum(nums, target))  # Output: 1 (subarray [8])


# =========================================================================================

'''
Two-Pointer Technique
Concept
The Two-Pointer technique involves using two indices (pointers) that move towards each other or in the same direction to solve problems efficiently.

When to Use:

When you need to compare pairs of elements in an array.
Sorting, searching, or solving for specific conditions between elements.
Key Idea: Use two pointers to narrow down or explore the solution space instead of using nested loops.
'''

# 1. Pair with Target Sum
# Problem: Find two numbers in a sorted array that add up to a given target.


def pair_with_target_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Increase the smaller pointer
        else:
            right -= 1  # Decrease the larger pointer

    return []


# Example:
nums = [1, 2, 3, 4, 6]
target = 6
print(pair_with_target_sum(nums, target))  # Output: [1, 3] (2 + 4 = 6)

# =============================================================================

# 2. Dutch National Flag Problem
# Problem: Sort an array with elements 0, 1, and 2 without using any sorting algorithm.


def dutch_flag_sort(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Example:
nums = [2, 0, 2, 1, 1, 0]
dutch_flag_sort(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

# =================================================================

# 3. Container With Most Water
# Problem: Given an array where each element represents the height of a line, find the maximum water that can be trapped.


def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        max_area = max(max_area, width * min(heights[left], heights[right]))

        # Move the shorter line inward
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Example:
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(heights))  # Output: 49

'''
Comparison of Sliding Window and Two-Pointer Techniques
=======================================================

Technique |	Key Use Cases |	Key Features
Sliding Window |	Contiguous subarrays or substrings |	Single pointer adjusts window size
Two-Pointer	Pair | comparisons, non-contiguous subarrays |	Two pointers move based on conditions
'''

# =============================================================================

'''
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. 
For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, 
or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). 
Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.
'''

str_letters = "abc",
array_shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]


def shiftingLetters(letters, shifts):
    """
    :type s: str
    :type shifts: List[List[int]]
    :rtype: str
    """
    alphabets = string.ascii_lowercase

    n = len(shifts)
    diff = [0] * (n + 1)  # Difference array

    # Apply the shifts to the difference array
    for start, end, direction in shifts:
        if direction == 1:  # Forward shift
            diff[start] += 1
            diff[end + 1] -= 1
        else:  # Backward shift
            diff[start] -= 1
            diff[end + 1] += 1

    # Compute the cumulative shift
    cumulative_shift = 0
    for i in range(n):
        cumulative_shift += diff[i]
        diff[i] = cumulative_shift  # Store cumulative shift in the same array

    # Apply the shifts to the string
    result = []
    for i in range(n):
        # Calculate the new character with wrapping
        shift = diff[i] % 26  # Wrap shift around the alphabet
        new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        result.append(new_char)

    return ''.join(result)


# Example Usage
s = "abc"
shifts = [[0, 1, 1], [1, 2, 0]]
print(shiftingLetters(s, shifts))  # Output: "ace"
