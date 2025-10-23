Feature: Build Array from Permutation

  # SRC: https://leetcode.com/problems/build-array-from-permutation/
  #
  # Constraints:
  # - `1 <= nums.length <= 1000`
  # - `0 <= nums[i] < nums.length`
  # - The elements in `nums` are distinct.

  Scenario Outline: Examples
    Given a zero-based permutation <nums> array (0-indexed)
    When build_array_from_permutation is invoked
    Then it returns an array <ans>wer
    # where ans[i] = nums[nums[i]]

    Examples:
    |       nums    |      ans      |
    | [0,2,1,5,3,4] | [0,1,2,4,5,3] |
    | [5,0,1,2,3,4] | [4,5,0,1,2,3] |
