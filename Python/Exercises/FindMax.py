def find_max(nums):
    maxx = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > maxx:
            maxx = nums[i]

    return maxx


if __name__ == "__main__":
    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    maxx = find_max(nums)
    print(maxx)
