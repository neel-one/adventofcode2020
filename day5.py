def solve(debug=False):
    sid = -1
    d = {}
    for i in range(1, 127): d[i] = []
    with open('day5.txt', 'r') as f:
        for line in f:
            lb = 0
            ub = 128
            line = line.strip('\n')
            for i in range(7):
                if line[i] == 'F':
                    ub = (ub-1 + lb)//2 + 1
                else:
                    lb = (ub-1 + lb)//2 + 1
                if debug: print(line[i], lb, ub)
            row = lb
            if debug: print(row)
            lb = 0
            ub = 8
            for i in range(7, 10):
                if line[i] == 'L':
                    ub = (ub-1 + lb)//2 + 1
                else:
                    lb = (ub-1 + lb)//2 + 1
            col = lb
            if debug: print(col)
            if debug: print(f'Sid: {row*8 + col}')
            sid = max(sid, row*8 + col)
            d[row].append(col)
    for i in range(1, 127):
        if len(d[i]) == 8: continue
        d[i].sort()
        for j in range(1, len(d[i])):
            if d[i][j] - 1 != d[i][j-1]:
                return 8*i +  d[i][j] - 1

    return sid

print(solve())