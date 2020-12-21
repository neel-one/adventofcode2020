def solve(debug=False):
    d = {1:0, 2:0, 3:1}
    nums = []
    with open('day10.txt', 'r') as f:
        for line in f:
            nums.append(int(line))
    nums.sort()
    alg(nums, d, 0)
    return 'See printed'

'''
Side Note: I love how sorting before the algorithm literally made it exponentially faster
'''
def alg(nums, d, rating):
    if len(nums) == 0: 
        print(d[1]*d[3])
        raise Exception
    for i in range(len(nums)):
        val = nums[i]
        if val - rating > 0 and val - rating <= 3:
            d[val-rating] += 1
            nums[i], nums[-1] = nums[-1], nums[i]
            nums.pop()
            alg(nums, d, val)
            nums.append(val)
            nums[i], nums[-1] = nums[-1], nums[i]
            d[val-rating] -= 1

def solve2(debug=False):
    nums = []
    with open('day10.txt', 'r') as f:
        for line in f:
            nums.append(int(line))
    nums.sort()
    ways = [0]*len(nums)
    for i in range(0, len(nums)):
        if nums[i] <= 3:
            ways[i] = 1   
    for i in range(1,len(nums)):
        j = 1
        while i-j >= 0 and nums[i] - nums[i-j] <= 3:
            ways[i] += ways[i-j]
            j += 1
    if debug: print(nums)
    if debug: print(ways)
    return ways[-1]
'''
My recursive algorithm simply doesn't work --> This is 100% a DP problem
Note from 10 minutes later - DP is way easier and much more efficient
'''
def alg2(nums, rating, mx, total):
    for i in range(len(nums)):
        val = nums[i]
        if val - rating > 0 and val - rating <= 3:
            if val == mx:
                total[0] += 1
            nums[i], nums[-1] = nums[-1], nums[i]
            nums.pop()
            alg2(nums, val, mx, total)
            nums.append(val)
            nums[i], nums[-1] = nums[-1], nums[i]

print(solve2())