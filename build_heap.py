# python3
# 201RMC092 Ernsts Strojevs 16.grupa

def heap_sort(data):
    def sift_down(i, n, swaps):
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
            sift_down(min_index, n, swaps)

    swaps = []
    n = len(data)

    # build heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n, swaps)

    # perform heap sort
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        sift_down(0, i, swaps)

    return swaps


def main():
    # read input
    input_type = input()
    if input_type.lower() == 'i':
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type.lower() == 'f':
        file_path = input()
        with open(f"tests/{file_path}", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    
    # perform heap sort
    swaps = heap_sort(data)

    # output result
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
