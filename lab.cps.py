def second_largest(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    n = len(unique_nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unique_nums[j] < unique_nums[j + 1]:
                unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]
nums = [4, 1, 3, 2, 4, 5, 3, 2, 1]
print("Second largest number is:", second_largest(nums))


def majority_element(nums):
    counts = {}

    # Count occurrences of each element
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Find the element with count greater than half the size of the list
    for num in counts:
        if counts[num] > len(nums) // 2:
            return num

# Example usage
nums = [3, 2, 3]
print("Majority element is:", majority_element(nums))


Postfix Conversions:

1. Expression: (A - B) * (C + D / E)
   Postfix: A B - C D E / + *

2. Expression: A / (B + C) * (D - E)
   Postfix: A B C + / D E - *

3. Expression: A * B - (C + D * E / F)
   Postfix: A B * C D E * F / + -


