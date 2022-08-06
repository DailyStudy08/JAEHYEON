# select_sort
N = int(input())
nums =[]
for _ in range(N):
    num = int(input())
    nums.append(num)


for i in range(len(nums)):
    min_index = i
    for j in range(i + 1, len(nums)):
        if nums[min_index] > nums[j]:
            min_index = j
    nums[min_index], nums[i] = nums[i], nums[min_index]

for n in nums:
    print(n)