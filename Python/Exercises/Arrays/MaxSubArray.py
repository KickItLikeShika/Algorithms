def MaxSubArray(nums, low, high):
    if low == high:
        return nums[low]
    else:
        mid = (low + high) // 2

        return max(MaxSubArray(nums, low, mid),
                   MaxSubArray(nums, mid+1, high),
                   MaxCrossingSubArray(nums, low, mid, high))


def MaxCrossingSubArray(nums, low, mid, high):
    left_sum, summ = -100000, 0
    for i in range(mid, low-1, -1):
        summ += nums[i]
        if summ > left_sum:
            left_sum = summ

    right_sum, summ = -100000, 0
    for j in range(mid + 1, high):
        summ += nums[j]
        if summ > right_sum:
            right_sum = summ

    return max(right_sum + left_sum, right_sum, left_sum)


if __name__ == "__main__":
    # The max sub array should be 43, the sum of
    # 18 + 20 + (-7) + 12
    nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    summ = MaxSubArray(nums, 0, len(nums) - 1)
    print(summ)
