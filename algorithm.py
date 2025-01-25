def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
                return 0

        unique_nums = set(nums)
        print(unique_nums)

        longest_streak = 0

        for num in unique_nums:
                if num - 1 is not unique_nums:
                        current_num = num
                        current_streak = 1

                        while current_num + 1 in unique_nums:
                                current_num += 1
                                current_streak += 1
                    
                        longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))