# Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

# Example 1:

# Input:
# N = 7, K = 4
# A[] = {1,2,1,3,4,2,3}

# Output: 3 4 4 3

# Explanation: Window 1 of size k = 4 is
# 1 2 1 3. Number of distinct elements in
# this window are 3. 
# Window 2 of size k = 4 is 2 1 3 4. Number
# of distinct elements in this window are 4.
# Window 3 of size k = 4 is 1 3 4 2. Number
# of distinct elements in this window are 4.
# Window 4 of size k = 4 is 3 4 2 3. Number
# of distinct elements in this window are 3.


N = 7
K = 4
a=[1,2,1,3,4,2,3]
def countDistinct(a, s, k):
    i=0
    j=0
    di={}
    c=0
    arr=[]
    while(j<s):
        if(a[j] not in di):
            di[a[j]]=0
        di[a[j]]+=1
        
        if(di[a[j]]==1):
            c=c+1
        if((j-i+1)==k):
            arr.append(c)
            di[a[i]]-=1
            if(di[a[i]]==0):
                del di[a[i]]
                c=c-1
            i+=1
        j+=1
    return arr

print(countDistinct(a,N,K))