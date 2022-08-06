N = input()
nums = []
for n in N:
    nums.append(int(n))

for i in range(len(nums)):
    min_index = i
    for j in range(i + 1, len(nums)):
        if nums[min_index] < nums[j]:
            min_index = j
    temp = nums[min_index] 
    nums[min_index] = nums[i]
    nums[i] = temp

array = list(map(str, nums))

ans = ('').join(array)
print(ans)
