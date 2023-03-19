# python3
# 201RMC092 Ernsts Strojevs 16. grupa


def build_heap(data):
    swaps = []
    n = len(data)

    # start from the last non-leaf node and heapify in reverse order
    for i in range(n//2-1, -1, -1):
        j = i
        while True:
            # find the index of the largest element among the node and its children
            left = 2*j+1
            right = 2*j+2
            largest = j
            if left < n and data[left] > data[largest]:
                largest = left
            if right < n and data[right] > data[largest]:
                largest = right
            
            # if the largest element is not the node itself, swap them and update the swaps array
            if largest != j:
                data[j], data[largest] = data[largest], data[j]
                swaps.append((j, largest))
                j = largest
            else:
                break
                
    return swaps


def heap_sort(data):
    n = len(data)
    swaps = build_heap(data)
    
    # repeatedly swap the largest element with the last element of the heap and heapify the remaining elements
    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        j = 0
        while True:
            # find the index of the largest element among the node and its children
            left = 2*j+1
            right = 2*j+2
            largest = j
            if left < i and data[left] > data[largest]:
                largest = left
            if right < i and data[right] > data[largest]:
                largest = right
            
            # if the largest element is not the node itself, swap them and update the swaps array
            if largest != j:
                data[j], data[largest] = data[largest], data[j]
                swaps.append((j, largest))
                j = largest
            else:
                break
                
    return swaps


def main():
    # read input from keyboard or file
    input_type = input("Enter input type (K for keyboard, F for file): ")
    if input_type.upper() == "K":
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements separated by spaces: ").split()))
    elif input_type.upper() == "F":
        filename = input("Enter the input file name: ")
        with open(filename, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input type")
        return

    # check if length of data is the same as the said length
    assert len(data) == n

    # call heap sort function to sort the data and get the swaps made during the sorting process
    swaps = heap_sort(data)

    # output the number of swaps made and the swaps themselves
    print("Number of swaps:", len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()