# python3
# 201RMC092 Ernsts Strojevs 16.grupa

import os
from typing import List, Tuple


def build_heap(data: List[int]) -> List[Tuple[int, int]]:
    swaps = []
    n = len(data)

    for i in range(n//2-1, -1, -1):
        j = i
        while True:
            left = 2*j+1
            right = 2*j+2
            largest = j
            
            if left < n and data[left] > data[largest]:
                largest = left
            if right < n and data[right] > data[largest]:
                largest = right
                
            if largest != j:
                data[j], data[largest] = data[largest], data[j]
                swaps.append((j, largest))
                j = largest
            else:
                break
                
    return swaps


def read_data_from_input() -> Tuple[str, List[int]]:
    mode = input().strip()
    if mode == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif mode == "F":
        file_name = input().strip()
        file_path = os.path.join("./tests", file_name)
        with open(file_path, "r") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
    else:
        raise ValueError("Invalid mode")
    return mode, data


def print_swaps(swaps: List[Tuple[int, int]]) -> None:
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


def main() -> None:
    mode, data = read_data_from_input()
    swaps = build_heap(data)
    print_swaps(swaps)


if __name__ == "__main__":
    main()
