'''Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}  
Output:
 5  
Explanation:
  
5 is the largest element in the array.

Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}  
Output:
 10  
Explanation:
  
10 is the largest element in the array.'''

# Brute Force Approach:

def largest_element_brute_force(arr):
    sorted(arr)
    return arr[-1]

# Time Complexity: O(n log n) due to sorting the array
# Space Complexity: O(1)


# ------------------------------------------------------------------------------------------

# Optimal Approach:
def largest_element_optimal(arr):
    max_element = arr[0]
    for n in arr:
        if n > max_element:
            max_element = n
    return max_element


# Time Complexity: O(n) as we traverse the array once
# Space Complexity: O(1) as we are using only a constant amount of space