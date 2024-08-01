# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.
# NOTE: A subarray is a contiguous part of any given array.

# Example 1:
# Input:
# N = 4, K = 2
# Arr = [100, 200, 300, 400]

# Output:
# 700
# Explanation:
# Arr3  + Arr4 =700,
# which is maximum.

def maximumSumSubarray (k,arr,N):
    max_sum=0
    summ=0
    i=0
    j=0
    while(j<N):
        summ=summ+arr[j]
        if((j-i+1)==k):
            if(summ>max_sum):
                max_sum=summ
            summ=summ-arr[i]
            i=i+1
        j=j+1
        
    return(max_sum)
N = 4
K = 2
Arr = [100, 200, 300, 400]
print(maximumSumSubarray(K,Arr,N))