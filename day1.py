

def solve(sum_):
    with open('day1.txt', 'r') as f:
        s = set()
        for line in f:
            line = int(line)
            if line in s:
                return (line * (sum_-line))
            else:
                s.add(sum_-line)
    return None


with open('day1.txt', 'r') as f:
    s = set()
    for line in f:
        line = int(line)
        subproblem = solve(2020-line)
        if subproblem is not None:
            print(line * subproblem)
            exit(0)
