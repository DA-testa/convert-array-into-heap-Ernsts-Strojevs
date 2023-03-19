# python3
# 201RMC092 Ernsts Strojevs 16.grupa

def heap_sort(data):
    n = len(data)
    swaps = []
    
    # heapify the array
    for i in range(n // 2, -1, -1):
        sift_down(data, i, n, swaps)
    
    # sort the array
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        sift_down(data, 0, i, swaps)
    
    return swaps

def sift_down(data, i, n, swaps):
    min_index = i
    left_child = 2 * i + 1
    if left_child < n and data[left_child] > data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < n and data[right_child] > data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, n, swaps)

def main():
    file_or_no = input("Enter I for keyboard input or F for file input: ")
    if file_or_no.lower() == 'i':
        n = int(input("Enter the length of the array: "))
        data = list(map(int, input("Enter space-separated integers: ").split()))
    elif file_or_no.lower() == 'f':
        file_name = input("Enter the name of the file: ")
        with open(file_name, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    
    # check if data has the expected length
    assert len(data) == n
    
    # sort the array and get swaps
    swaps = heap_sort(data)
    
    # output the number of swaps and each swap
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
