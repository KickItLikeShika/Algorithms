def find_min(nums):
    minn = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < minn:
            minn = nums[i]

    return minn


if __name__ == "__main__":
    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    minn = find_min(nums)
    print(minn)
