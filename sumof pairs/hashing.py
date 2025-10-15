def hashing(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

if __name__ == "__main__":
    arr = [2, 7, 11, 15, 1, 8, 3]
    target = 9
    print("Hashing:", hashing(arr, target))