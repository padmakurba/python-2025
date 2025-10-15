def binary_search(arr, target):
    def bin_search(arr, x, start):
        left, right = start, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    pairs = []
    arr.sort()
    n = len(arr)
    for i in range(n):
        complement = target - arr[i]
        idx = bin_search(arr, complement, i + 1)
        if idx != -1:
            pairs.append((arr[i], arr[idx]))
    return pairs

if __name__ == "__main__":
    arr = [2, 7, 11, 15, 1, 8, 3]
    target = 9
    print("Binary Search:", binary_search(arr, target))