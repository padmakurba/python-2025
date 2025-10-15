def recursive_binary_search(arr, x, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return recursive_binary_search(arr, x, mid + 1, right)
    else:
        return recursive_binary_search(arr, x, left, mid - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 7, 8, 11, 15]
    target = 8
    idx = recursive_binary_search(arr, target, 0, len(arr) - 1)
    print("Recursive Binary Search: Index =", idx)