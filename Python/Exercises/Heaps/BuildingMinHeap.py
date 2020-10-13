import heapq


def parent(i):
    return (i-1) // 2


def right(i):
    return (i * 2) + 2


def left(i):
    return (i*2) + 1


def build_min_heap(nums):
    for i in range(len(nums) // 2, -1, -1):
        min_heapify(nums, i)


def min_heapify(nums, i):
    l = left(i)
    r = right(i)
    smallest = -100000
    if l < len(nums) and nums[l] < nums[i]:
        smallest = l
    else:
        smallest = i

    if r < len(nums) and nums[r] < nums[smallest]:
        smallest = r

    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        min_heapify(nums, smallest)


if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    nums3 = [16, 17, 18, 19, 20, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    nums4 = [16, 17, 18, 19, 20, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # min heap
    heapq.heapify(nums3)
    print("MIN heap from built in heapq: ")
    print(nums3)

    build_min_heap(nums4)
    print("MIN heap manually implemented: ")
    print(nums4)
