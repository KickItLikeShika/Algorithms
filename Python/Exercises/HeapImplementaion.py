import heapq


def parent(i):
    return (i-1) // 2


def right(i):
    return (i * 2) + 2


def left(i):
    return (i*2) + 1


def max_heapify(listForTree, i):
    l = left(i)
    r = right(i)

    if l <= len(listForTree) and listForTree[l] > listForTree[i]:
        largest = l
    else:
        largest = i
    
    if r <= len(listForTree) and listForTree[r] > listForTree[largest]:
        largest = r
    
    if largest != i:
        listForTree[i], listForTree[largest] = listForTree[largest], listForTree[i]
        max_heapify(listForTree, i)


if __name__ == "__main__":
    pass
    listForTree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # listForTree = [16, 17, 18, 19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # min heap
    # heapq.heapify(listForTree) 
    # print(listForTree)

    # max heap
    heapq._heapify_max(listForTree)  
    print(listForTree)
