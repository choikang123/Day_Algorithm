def solution(nums):
    box_len=len(nums)//2
    nums=set(nums)
    nums_len=len(nums)

    if box_len<=nums_len:
        return box_len
    elif box_len>=nums_len:
        return nums_len