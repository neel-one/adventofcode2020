def solve(debug=False):
    nums = []
    with open('day9.txt', 'r') as f:
        for line in f:
            nums.append(int(line))
    for i in range(26,len(nums)):
        sub = nums[i-25:i]
        if debug: print(len(sub))
        valid = twosum(sub, nums[i])
        if not valid: return nums[i]
    return -1

def twosum(nums, target):
    s = set()
    for i in nums:
        if i in s:
            if i*2 != target:
                return True
        else:
            s.add(target-i)
    return False

def solve2(target,debug=False):
    nums = []
    with open('day9.txt', 'r') as f:
        for line in f:
            nums.append(int(line))
    i = 0
    j = 1
    s = nums[i] + nums[j]
    while s != target:
        if s < target:
            j += 1
            s += nums[j]
        else:
            s -= nums[i]
            i += 1
    if debug: print(i,j)
    mn = float('inf')
    mx = -float('inf')
    for i in range(i, j+1):
        mn = min(mn, nums[i])
        mx = max(mx, nums[i])
    return mn+mx
print(solve2(258585477))