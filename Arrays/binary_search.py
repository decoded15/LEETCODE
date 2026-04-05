'''

Problem: Binary Search Implementation
Approach: Iterative Binary Search (Closed Interval)
Time Complexity: O(log n)
Space Complexity: O(1)

Binary search is an efficient algorithm for finding an item from a sorted list of items. 
It works by repeatedly dividing in half the portion of the list that could contain the item 
until you've narrowed down the possible locations to just one.

Example:
Input: nums = [1, 3, 5, 7, 9, 11, 13], target = 7
Output: 3

'''

def binary_search(nums, target):
    """
    Search for a target value in a sorted array using binary search.
    :param nums: List[int] - A sorted list of integers.
    :param target: int - The value to search for.
    :return: int - The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Check if target is present at mid
        if nums[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif nums[mid] < target:
            low = mid + 1
            
        # If target is smaller, ignore the right half
        else:
            high = mid - 1

    # Target was not found in the array
    return -1

# Simple test case for verification
if __name__ == "__main__":
    test_nums = [1, 3, 5, 7, 9, 11, 13]
    test_target = 7
    result = binary_search(test_nums, test_target)
    print(f"Index of {test_target} in {test_nums}: {result}")
