from typing import List

def two_elements(sorted_arr: list[int], target: int):
    left, right =  0, len(sorted_arr) - 1
    while left < right:
        if sorted_arr[left] + sorted_arr[right] == target:
            return [left, right]
        elif sorted_arr[left] + sorted_arr[right] < target:
            left += 1
        else:
            right -= 1
    return False

def main():
    arr = [16, 30, 40, 50, 60, 71]
    target = 90
    print(two_elements(arr, target))

if __name__ == "__main__":
    main()
