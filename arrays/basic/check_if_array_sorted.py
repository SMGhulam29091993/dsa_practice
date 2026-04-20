'''
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.
Here element 5 is not smaller than or equal to its future elements.
'''

# Brute Force Approach:
def is_array_sorted_brute_force(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                return False
    return True

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# -------------------------------------------------------------------------------------------


# Optimal Approach:
def is_array_sorted_optimal(arr):
    for i in range(1, len(arr)-1):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Time Complexity: O(n)
# Space Complexity: O(1)