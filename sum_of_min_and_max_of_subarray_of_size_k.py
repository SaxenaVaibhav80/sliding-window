# sum_of_min_and_max_of_subarray_of_size_k--

#test cases--->
# arr=[2, 5, -1, 7, -3, -1, -2] k = 4 output=[6,4,4,4]
# arr=[1, 3, 1, 2, 0, 5] k=3 output=[4, 4, 2, 5]
# arr=[9, 7, 2, 3, 6, 1, 8] k=5 output=[11, 9, 8, 7, 9]
nums=[-5, -2, -1, 0, 3, 6]  
k=3
i=0
j=0
maxi=float("-inf")
mini=float("+inf")
summ=0
arr2=[]
sum2=0
maxx=[]
minn=[]
s=len(nums)
while(j<s):
    if(maxx and nums[j]>maxx[-1]):
        while(maxx and maxx[-1]<nums[j]):
            maxx.pop()
    maxx.append(nums[j])
    
    if(minn and minn[-1]>nums[j]):
        while(minn and minn[-1]>nums[j]):
            minn.pop()
    minn.append(nums[j])
    
    if((j-i+1)==k):
        sum2=minn[0]+maxx[0]
        if(nums[i]==maxx[0]):
            maxx.pop(0)
    
        if(nums[i]==minn[0]):
            minn.pop(0)
        i=i+1
        arr2.append(sum2)
    j=j+1
    
print(arr2)