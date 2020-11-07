def insertion_sort_decreasing(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        i = j - 1
        while i > -1 and key > nums[i]:
            nums[i+1] = nums[i]
            i -= 1
        nums[i+1] = key


if __name__ == "__main__":
    nums = [5, 2, 4, 6, 1, 3]
    insertion_sort_decreasing(nums)
    print(nums)
