# python3
# 201RMC092 Ernsts Strojevs 16.grupa

def build_heap(data_list):
    n = len(data_list)
    swap_list = []
    for i in range(n):
        while i > 0:
            parent = (i - 1) // 2
            if data_list[i] <= data_list[parent]:
                break
            data_list[i], data_list[parent] = data_list[parent], data_list[i]
            swap_list.append((parent, i))
            i = parent
    return swap_list

def main():
    input_type = input()
    if "I" in input_type or "i" in input_type:
        num_elements = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_type or "f" in input_type:
        input_file = input()
        if "a" not in input_file:
            with open("tests/" + input_file, 'r') as f:
                num_elements = int(f.readline())
                data = list(map(int, f.readline().split()))

    assert len(data) == num_elements

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
