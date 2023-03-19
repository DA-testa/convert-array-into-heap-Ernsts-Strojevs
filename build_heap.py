# python3
# 201RMC092 Ernsts Strojevs 16.grupa

def build_heap(data):
    n = len(data)
    swaps = []

    for i in range(n // 2, -1, -1):
        min_heapify(data, i, n, swaps)

    return swaps

def min_heapify(data, i, n, swaps):
    l = 2 * i + 1
    r = 2 * i + 2
    min = i

    if l < n and data[l] < data[min]:
        min = l

    if r < n and data[r] < data[min]:
        min = r

    if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        min_heapify(data, min, n, swaps)

def main():
    input = input()

    if "I" in input or "i" in input:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in input or "f" in input:
        file_path = input()

        if "a" not in file_path:
            with open("tests/" + file_path, 'r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))

    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
