import heapq


def parent(i):
    return (i-1) // 2


def right(i):
    return (i * 2) + 2


def left(i):
    return (i*2) + 1


def max_heapify(nums, i):
    l = left(i)
    r = right(i)
    largest = -100000
    if l <= len(nums) and nums[l] > nums[i]:
        largest = l
    else:
        largest = i

    if r <= len(nums) and nums[r] > nums[largest]:
        largest = r

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums, i)


if __name__ == "__main__":
    pass
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # nums = [16, 17, 18, 19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # min heap
    # heapq.heapify(nums)
    # print(nums)

    # max heap
    heapq._heapify_max(nums)
    print(nums)
