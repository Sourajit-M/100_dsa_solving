def two_sum(nums, target):
  map = {}

  for i in range(len(nums)):
    diff = target - nums[i]
    if diff in map:
      return [map[diff], i]
    
    map[nums[i]] = i

  return [-1, -1]

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Indices of the two numbers that add up to {target}: {result}")