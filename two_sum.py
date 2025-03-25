def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

    num_dict = {}
    for i, num in enumerate(nums):
        print(f'Num: {num}')
        print(f'Indices: {i}')
        complement = target - num

        if complement in num_dict:
            return [num_dict[complement], i]

        num_dict[num] = i


print(twoSum([1, 2, 3], 5))
