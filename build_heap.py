# python3
# 201RMC092 Ernsts Strojevs 16.grupa

def heap_sort(arr):
    def heapify(arr, n, i, swaps):
        largest = i  
        l = 2 * i + 1     
        r = 2 * i + 2     
     
        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps.append((i, largest))
            heapify(arr, n, largest, swaps)

    swaps = []
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i, swaps)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swaps.append((0, i))
        heapify(arr, i, 0, swaps)

    return swaps

def main():
    # get input from user or file
    input_type = input()
    if input_type == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type == 'F':
        file_path = input()
        with open(file_path, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input type!")
        return

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data and give back all swaps
    swaps = heap_sort(data)

    # output how many swaps were made
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
