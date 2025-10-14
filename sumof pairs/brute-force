nums=[1,2,3,4,5,6]
target_sum=5
pair=[]
#output =[0,1]
#explanation: because nums[0]+nums[1] ==5,we return[0,1]
def two_sum_brute_force(nums, target_sum):
    n=len(nums)
    for i in range(n):         
        for j in range(i+1, n): #avoid checking the same element twice
            if nums[i] + nums[j] == target_sum:
                pair.append((nums[i], nums[j])) #return pairs of sum
            
        
    return pair  #return empty list if no solution found

result=two_sum_brute_force(nums, target_sum)
print(nums)
print("All pair whose sum is equal to: ",target_sum,"is\n",result)