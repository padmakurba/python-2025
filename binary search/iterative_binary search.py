def iterative_binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 7, 8, 11, 15]
    target = 8
    idx = iterative_binary_search(arr, target)
    print("Iterative Binary Search: Index =", idx)