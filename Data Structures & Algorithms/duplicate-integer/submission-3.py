class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = set()

        for n in nums:
            if n in new_list:
                return True
            new_list.add(n)
        return False