def find_median(nums1, nums2):
    """
    Finds the median of two sorted arrays with a time complexity of O(log (m+n)).
    :param nums1: List[int] - First sorted array
    :param nums2: List[int] - Second sorted array
    :return: float - Median of the two sorted arrays
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        # Handle edge cases for partitions
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == x else nums1[partition_x]

        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == y else nums2[partition_y]

        # Check if we have found the correct partition
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If the total number of elements is odd
            if (x + y) % 2 == 1:
                return max(max_left_x, max_left_y)
            # If the total number of elements is even
            return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
        elif max_left_x > min_right_y:
            # Move towards the left in nums1
            high = partition_x - 1
        else:
            # Move towards the right in nums1
            low = partition_x + 1

    raise ValueError("Input arrays are not sorted or invalid.")
