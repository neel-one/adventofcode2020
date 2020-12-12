def solve(debug=False):
    ans = ['']
    with open('day6.txt', 'r') as f:
        for line in f:
            line = line[:-1] + ' '
            if line.split() == []:
                ans.append('')
            else:
                ans[-1] += line
    total = 0
    for string in ans:
        d = dict()
        l = string.split() #separate each answer within each group
        for s in l:
            for char in s: 
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
        for key in d:
            if d[key] == len(l):
                total += 1
        if debug: print(s)
        #total += len(s)
    return total

print(solve())
