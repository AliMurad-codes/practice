# Q#1:
def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k
nums = [1, 1, 2, 2, 3, 4, 4, 5]
k = remove_duplicates(nums)
print(f"The number of unique elements is: {k}")
print(f"The array after removing duplicates: {nums[:k]}")

# Q#2:


nums = [2, 7, 11, 15]
target = 9
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"The indices of the two numbers that add up to {target} are: [{i}, {j}]")
            break
    else:
        continue
    break

# Q#3:

nums = [3, 4, -1, 1]
positive_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)
positive_nums.sort()
smallest_missing = 1
for num in positive_nums:
    if num == smallest_missing:
        smallest_missing += 1
    elif num > smallest_missing:
        break
print(f"The smallest positive integer not present in the array is: {smallest_missing}")

# Q#4

num = [1, 0, 4, 3, 0, 6, 7, 5]
non_zero_elements = []
for i in range(len(num)):
    if num[i] != 0:
        non_zero_elements.append(num[i])
zero_count = len(num) - len(non_zero_elements)
for i in range(zero_count):
    non_zero_elements.append(0)
num = non_zero_elements
print(num)



