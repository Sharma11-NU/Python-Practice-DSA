"""
To find the maximum product,
that is multiplying the two biggest numbers in the list.

"""
def max_pairwise_product(nums):
    n = len(nums)
    if n < 2:
        return 0

# Find the index of the largest number
    max_index1 = 0
    for i in range(1, n):
        if nums[i] > nums[max_index1]:
            max_index1 = i

# Find the index of the second-largest number
    max_index2 = -1
    for i in range(n):
        if i != max_index1 and (max_index2 == -1 or nums[i] > nums[max_index2]):
            max_index2 = i

    return nums[max_index1] * nums[max_index2]


if __name__ == '__main__':
    _ = int(input())
    input_nums = list(map(int, input().split()))
    print(max_pairwise_product(input_nums))


#--------------- ANOTHER WAY------------------------------

def max_pairwise_product(nums):
    n = len(nums)
    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_product = max(max_product,
                nums[i] * nums[j])

    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_nums = list(map(int, input().split()))
    print(max_pairwise_product(input_nums))
