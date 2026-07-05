class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []

        for n in nums:
            if n not in new_list:
                new_list.append(n)
            else:
                return True
        return False