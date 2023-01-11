#**Problem 00001: Two sum**

#**Example 1:**

nums = [2,7,11,15]
target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


#**First attempt**

#Nested loops

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  #input parameters
            for i in range(len(nums)):                            #first loop
                 for j in range(i+1, len(nums)):                  #take i+1 value
                    if nums[i] + nums[j] == target:               # if sum is target ==> solution
                        return [i,j]
 
 #Quick, simple solution but slow in execution, since here two lists are nested and thus the time is squared.
 
 #Insert better solution:still to continue
