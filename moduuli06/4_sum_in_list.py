def sum_nums_in_list(nums):
    total = 0
    for num in nums:
        total += num
    return total


def main():
    list1 = [1, 22, 53, 4677, 5, 565]
    print(sum_nums_in_list(list1))


main()
