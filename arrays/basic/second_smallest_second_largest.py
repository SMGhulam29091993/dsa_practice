'''
Find Second Smallest and Second Largest Element in an array


43

Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Examples
Example 1:
Input:
 [1, 2, 4, 7, 7, 5]  
Output:
  
Second Smallest : 2  
Second Largest : 5  
Explanation:
  The elements are sorted as 1, 2, 4, 5, 7, 7.  
Hence, the second smallest element is 2, and the second largest element is 5.

Example 2:
Input:
 [1]  
Output:
  
Second Smallest : -1  
Second Largest : -1  
Explanation:
  Since there is only one element in the array, it is both the largest and smallest element.  
Therefore, there is no second smallest or second largest element present.'''

# Brute Force Approach:
def find_second_smallest_and_second_largest_brute_force(arr):
    sorted(arr)
    second_smallest = arr[1] if len(arr) > 1 else -1
    second_largest = arr[-2] if len(arr) > 1 else -1
    return second_smallest, second_largest

# Time Complexity: O(n log n) due to sorting the array
# Space Complexity: O(1)

# ------------------------------------------------------------------------------------------

# Optimal Approach:
def find_second_smallest_and_second_largest_optimal(arr):
    if len(arr) < 2:
        return -1, -1
    
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    for n in arr:
        # smallest and second smallest check
        if n < smallest:
            second_smallest = smallest
            smallest = n
        elif n < second_smallest and n != smallest:
            second_smallest = n
        # largest and second largest check
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest and n != largest:
            second_largest = n

    # If second smallest or second largest doesn't exist, return -1
    second_smallest = second_smallest if second_smallest != float('inf') else -1
    second_largest = second_largest if second_largest != float('-inf') else -1
    
    return second_smallest, second_largest

# Time Complexity: O(n)
# Space Complexity: O(1)