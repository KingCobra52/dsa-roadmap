# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list.
# The second function should be linear
#
def quadratic(nums):
    for i in range(len(nums)):
        is_smallest = True
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                is_smallest = False
                break

        if is_smallest:
            return nums[i]

def linear(nums):
    smallest = float('inf')
    for i in range(len(nums)):
        # if nums[i] < smallest:
        #     smallest = nums[i]
        smallest = min(smallest, nums[i])
    return smallest

def main():
    nums = [1, 2, 0, 4, 90, -9, 6, 7, 87]
    print(quadratic(nums))
    print(linear(nums))


if __name__ == "__main__":
    main()
