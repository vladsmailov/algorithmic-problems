def longestMonotonicSubarray(nums):
    if len(nums) == 1:
        return 1
    max_length = 1
    desc_length = 1
    asc_length = 1
    for index in range(1, len(nums)):
        if nums[index] > nums[index-1]:
            asc_length += 1
            desc_length = 1
        elif nums[index] < nums[index-1]:
            desc_length += 1
            asc_length = 1
        else:
            asc_length = 1
            desc_length = 1
        max_length = max(asc_length, desc_length, max_length)
    return max_length


nums = [1, 2, 4, 2, 1, 0]
print(longestMonotonicSubarray(nums))

# def longestMonotonicSubarray(nums):
#     result = []
#     temp = []
#     if len(nums) == 1:
#         return 1
#     for index in range(len(nums)):
#         if index == len(nums)-1:
#             print(nums[index])
#             if nums[index] > nums[index-1]:
#                 print(nums[index])
#                 temp.append(nums[index])
#                 result.append(len(temp))
#                 temp = []
#             continue
#         if nums[index] < nums[index+1]:
#             temp.append(nums[index])
#         else:
#             temp.append(nums[index])
#             result.append(len(temp))
#             temp = []
#     temp = []
#     for index in range(len(nums)):
#         if index == len(nums)-1:
#             if nums[index] < nums[index - 1]:
#                 temp.append(nums[index])
#                 result.append(len(temp))
#                 temp = []
#             continue
#         if nums[index] > nums[index+1]:
#             temp.append(nums[index])
#         else:
#             temp.append(nums[index])
#             result.append(len(temp))
#             temp = []
#     return max(result)
#
# nums = [2, 1, 3, 5, 6, 8]
# print(longestMonotonicSubarray(nums))