# python3
# 201RMC092 Ernsts Strojevs 16.grupa

def build_heap(data):
    n = len(data)
    swaps = []

    for i in range(n // 2, -1, -1):
        min_heapify(data, i, n, swaps)

    return swaps

def min_heapify(data, i, n, swaps):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    min_index = i

    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child

    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        min_heapify(data, min_index, n, swaps)

def main():
    input_mode = input()

    if "I" in input_mode or "i" in input_mode:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_mode or "f" in input_mode:
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
