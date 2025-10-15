def two_pointer(arr, target):
    pairs = []
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1
    return pairs

if __name__ == "__main__":
    arr = [2, 7, 11, 15, 1, 8, 3]
    target = 9
    print("Two Pointer:", two_pointer(arr, target))