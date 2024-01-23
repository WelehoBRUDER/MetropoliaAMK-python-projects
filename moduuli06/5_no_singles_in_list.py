def list_with_even_numbers(nums):
    even_numbers = []
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def main():
    list1 = [1, 22, 53, 4677, 5, 565, 4, 12]
    print(f"Alkuperäinen: {list1}")
    print(f"Tasaluvut: {list_with_even_numbers(list1)}")


main()
