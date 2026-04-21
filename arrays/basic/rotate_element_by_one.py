'''
Left Rotate the Array by One


21

Problem Statement: Given an integer array nums, rotate the array to the left by one.

Note: There is no need to return anything, just modify the given array.

Examples
Example 1:
Input:
 nums = [1, 2, 3, 4, 5]  
Output:
 [2, 3, 4, 5, 1]  
Explanation:
 Initially, nums = [1, 2, 3, 4, 5]  
Rotating once to the left results in nums = [2, 3, 4, 5, 1].

Example 2:
Input:
 nums = [-1, 0, 3, 6]  
Output:
 [0, 3, 6, -1]  
Explanation:
 Initially, nums = [-1, 0, 3, 6]  
Rotating once to the left results in nums = [0, 3, 6, -1].
'''

# Brute Force Approach
def left_rotate_array_by_one_brute_force(arr):
    initial_element = arr[0]
    dummy = arr[1:]
    dummy.append(initial_element)
    return dummy

# Time Complexity: O(n)
# Space Complexity: O(n)

# --------------------------------------------------------------------------------------------

# Optimal Approach
def left_rotate_array_by_one_optimal(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = temp
    return arr

# Time Complexity: O(n)
# Space Complexity: O(1)