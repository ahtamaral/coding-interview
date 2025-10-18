from datetime import datetime
from typing import List

"""
Complexity: O(n**2)

for i in range(0, len(list)):
    for j in range(i+1, len(list))
        if list[i]!= list[j]:
            if list[i] == list[j]:
                return [i, j]

dict.fromkeys(a, 0)

Why use dicts: Search complexity O(1), because it is implemented as a hash table.
"""

"""
myDict = {
    2: 0,
    7: 1,
    11: 2,
    15: 3
}
"""

start_time = datetime.now()

list = [5, 7, 11, 15, 3, 8, 16, 19, 2] 
target = 9

# enumerate(nums)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initialization step:  Creates a dictionary whose key is the list values and the value (int he sense of key-value pair) is the element's respective index.
        # Example
        #
        # list = [2, 7, 11, 15] 
        # myDict = { 2: 0,
        #            7: 1  ,
        #            11: 2,
        #            15: 3 }
        myDict = dict.fromkeys(nums, -1)
        for idx in range ( len(nums) ):
            myDict[ nums[idx] ] = idx

        # EDGE CASE: [3,3], answer [0,1].
        # On the Initialization step, the conversion of a list into a dict kills the information of a list having two elemnts of equal value on different indexes.
        # Need to think on that...

        print(f"Input dict: {myDict}")

        # Processing step: Will search if value and (target - value) both exists in the dictionary. Will do this for all values.
        for idx in range( len(nums) ):
            
            candidate1 = nums[idx]
            candidate2 = target - nums[idx]

            answerIdx1 = myDict.get( nums[idx], -1)
            answerIdx2 = myDict.get( target - nums[idx], -1)
            
            if answerIdx1 == answerIdx2:
                continue
            
            print(f"list[{idx}]: {nums[idx]}")

            if ( (answerIdx1 != -1) and
                 (answerIdx2 != -1) and
                 (candidate1 + candidate2 == target) ):
                print(f"answer: {[answerIdx1, answerIdx2]}")
                return [answerIdx1, answerIdx2]



list = [5, 7, 11, 15, 3, 8, 16, 19, 2] 
target = 9

list = [3, 3]
target = 6

sol = Solution()


print(f"Starting Solution.TwoSum() execution.")
start_time = datetime.now()

answer = sol.twoSum(list, target)

end_time = datetime.now()
time_difference = end_time - start_time

print(f"Time elapsed: {time_difference.total_seconds() * 1000:.1f} ms")

print(f"Answer: {answer}")

