# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

def findmaximum(A,B):
    i=0
    j=0
    arr=[]
    q=[]
    s=len(A)
    while(j<s):
        if(len(A)==0):
            return 0
        else:
            if(q and A[j]>q[-1]):
                while(q and q[-1]<A[j]):
                    q.pop()
            q.append(A[j])
            if((j-i+1)==B):
               if(A[i]==q[0]):
                   arr.append(q[0])
                   q.pop(0)
               else:
                   arr.append(q[0])      
               i=i+1
        j=j+1
    return arr
nums = [1,3,-1,-3,5,3,6,7]
print(findmaximum(nums,3))
        


