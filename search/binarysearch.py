

def binarysearch(arr, x):
    """Iterative binary search.
    Time Complexity: O(log N)
    Auxiliary Space: O(1)
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    data = [2, 3, 4, 10, 40]
    print(binarysearch(data, 10))
    print(binarysearch(data, 20))
    