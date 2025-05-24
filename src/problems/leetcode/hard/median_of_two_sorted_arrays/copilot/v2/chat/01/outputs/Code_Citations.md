# Code Citations

## License: unknown

https://github.com/Musabpirzada/Leetcode-problems/tree/a465560b536dbe6f389b10c700fa4f2485cb8a66/median_of_two_sorted_arrays.py

```
array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
```

## License: unknown

https://github.com/SharathN29/Leetcode/tree/11560c4ef0c48e03d37f040f7118f229c02a662c/Leetcode%20-%20Python/array_medianTwoSortedArray.py

```
:
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) //
```

## License: unknown

https://github.com/724thomas/CodingChallenge_Python/tree/6ca5950ec636066f76f95ad4a9ef60897f713b14/LeetCode/4.%20Median%20of%20Two%20Sorted%20Arrays.py

```
, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 -
```

## License: unknown

https://github.com/scyanh/needcode/tree/fc9c505263f5d812af21d35320342139fe9ba541/leetcode150/18_Binary%20Search/7_%28Hard%29%20Median%20of%20Two%20Sorted%20Arrays/main.py

```
('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]

            maxY = float('-inf') if partitionY == 0 else nums2[partitionY -
```
