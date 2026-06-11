class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicates = len(nums) != len(set(nums))
        return has_duplicates