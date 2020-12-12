def solve(debug=False):
    tree = {}
    with open('day7.txt', 'r') as f:
        for line in f:
            line = line.split()
            parent = line[0]+line[1]
            for i in range(2, len(line)):
                if line[i-3].isdigit():
                    child = line[i-2] + line[i-1]
                    if child in tree:
                        tree[child].append(parent)
                    else:
                        tree[child] = [parent]
    if debug: print(tree['shinygold'])
    ans = set(traverse(tree, 'shinygold'))
    if debug: 
        for i in ans: print(i)
    return len(ans)

def traverse(tree, key):
    ans = []
    if key not in tree:
        return [key]
    for val in set(tree[key]):
        ans += traverse(tree, val) + [val]
    return ans 

def solve2(debug=False):
    tree = {}
    with open('day7.txt', 'r') as f:
        for line in f:
            line = line.split()
            key = line[0]+line[1]
            for i in range(2, len(line)):
                if line[i-3].isdigit():
                    val = [line[i-2] + line[i-1]]*int(line[i-3])
                    if key in tree:
                        tree[key] += val
                    else:
                        tree[key] = val
    return traverse2(tree,'shinygold')
def traverse2(tree, key):
    ans = 0
    if key not in tree:
        return 0
    for val in tree[key]:
        ans += 1 + traverse2(tree, val)
    return ans 

print(solve2(0))