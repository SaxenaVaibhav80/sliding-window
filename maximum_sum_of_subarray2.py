# 2461. Maximum Sum of Distinct Subarrays With Length K

# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

# code-->

def maximumSubarraySum(nums,k):
    di = {}
    i = 0
    summ = 0
    maxi = float('-inf')
    s = len(nums)
    c = 0 
    for j in range(s):
        if nums[j] not in di:
            di[nums[j]] = 0
        di[nums[j]] =di[nums[j]] + 1
        summ =summ+ nums[j]
        if di[nums[j]] == 1:
            c =c+ 1
        if (j - i + 1) == k:
            if c == k:
                maxi = max(maxi, summ)
            summ = summ- nums[i]
            if di[nums[i]] == 1:
                c =c-1
            di[nums[i]] = di[nums[i]]- 1
            if di[nums[i]] == 0:
                del di[nums[i]]
            i =i+1
    if(maxi!= float('-inf')):
        return maxi
    else:
        return 0