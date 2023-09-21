class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2nd solution

        # declare hash
        hashtable = {}

        # time  O(n)
        # space O(n)
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashtable:
                return [hashtable[x], i]
            hashtable[nums[i]] = i
