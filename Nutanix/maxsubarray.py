# https://www.hackerrank.com/contests/s30-nutanix/challenges/maxsubarray

def maxSubarray(arr):
    max_subseq,max_subarr,max_ele=-10001,-10001,-10001
    is_all_neg=True
    pos_sum=0
    cur_sum=0
    for a in arr: 
        max_ele=max(max_ele,a)
        if a>=0:
            is_all_neg=False
            pos_sum+=a
        cur_sum+=a
        max_subarr=max(max_subarr, cur_sum)
        if cur_sum<0: cur_sum=0
    
    #all negative case
    if is_all_neg:
        return max_ele,max_ele
    #mix of pos and neg
    else:
        max_subseq=pos_sum
        return max_subarr,max_subseq



# We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

# Given an array, find the maximum possible sum among:

# all nonempty subarrays.
# all nonempty subsequences.
# Print the two values as space-separated integers on one line.

# Note that empty subarrays/subsequences should not be considered.

# Example

# The maximum subarray sum is comprised of elements at inidices . Their sum is . The maximum subsequence sum is comprised of elements at indices  and their sum is .

# Function Description

# Complete the maxSubarray function in the editor below.

# maxSubarray has the following parameter(s):

# int arr[n]: an array of integers
# Returns

# int[2]: the maximum subarray and subsequence sums
# Input Format

# The first line of input contains a single integer , the number of test cases.

# The first line of each test case contains a single integer .
# The second line contains  space-separated integers  where .

# Constraints

# The subarray and subsequences you consider should have at least one element.

# Sample Input 0

# 2
# 4
# 1 2 3 4
# 6
# 2 -1 2 3 4 -5
# Sample Output 0

# 10 10
# 10 11
# Explanation 0

# In the first case: The maximum sum for both types of subsequences is just the sum of all the elements since they are all positive.

# In the second case: The subarray  is the subarray with the maximum sum, and  is the subsequence with the maximum sum.

# Sample Input 1

# 1
# 5
# -2 -3 -1 -4 -6
# Sample Output 1

# -1 -1
# Explanation 1

# Since all of the numbers are negative, both the maximum subarray and maximum subsequence sums are made up of one element, .