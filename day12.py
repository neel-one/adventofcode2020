def solve():
    instr = []
    with open('day12.txt','r') as f:
        for line in f:
            instr.append(line)
    head = 'E'
    d = {'N':0,'S':0,'E':0,'W':0}
    dirs = ['N','E','S','W']
    for i in instr:
        action = i[0]
        val = int(i[1:])
        if action in dirs:
            d[action] += val
        elif action == 'F':
            d[head] += val
        else:
            idx = dirs.index(head)
            if action == 'R':
                head = dirs[(idx + val//90) % 4]
            else:
                head = dirs[(idx - val//90) % 4]
    if debug: print(d)
    return abs(d['N']-d['S']) + abs(d['E']-d['W'])

def solve2():
    instr = []
    with open(filename,'r') as f:
        for line in f:
            instr.append(line)
    dirs = ['N','S','E','W']
    d = {'N':0,'E':0}
    waypt = {'N':1, 'E':10}
    _waypt = {'N':0,'E':0}
    rotate = {'N':['N','E','S','W'],'E':['E','S','W','N']}
    for i in instr:
        action = i[0]
        val = int(i[1:])
        if action in dirs:
            if action == 'S':
                action = 'N'
                val *= -1
            elif action == 'W':
                action = 'E'
                val *= -1
            waypt[action] += val
        elif action == 'F':
            d['N'] += waypt['N']*val
            d['E'] += waypt['E']*val
        else:
            if action == 'R': newN = rotate['N'][val//90]
            else: newN = rotate['N'][-val//90]
            if newN == 'S' or newN == 'W': 
                waypt['N'] *= -1
                newN = dirs[dirs.index(newN)-1]
            if action == 'R': newE = rotate['E'][val//90]
            else: newE = rotate['E'][-val//90]
            if newE == 'S' or newE == 'W': 
                waypt['E'] *= -1
                newE = dirs[dirs.index(newE)-1]
            _waypt[newN] = waypt['N']
            _waypt[newE] = waypt['E']
            waypt = _waypt.copy()
        if debug: print(d, waypt)
    if debug: print(d)
    return abs(d['N']) + abs(d['E'])

filename = 'day12.txt'
debug = False
print(solve2())