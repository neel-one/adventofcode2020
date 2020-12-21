import copy
debug = False
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
def solve():
    mp = list()
    with open('day11.txt','r') as f:
        for line in f:
            line = [c for c in line if c != '\n']
            mp.append(line)
    debug_i = 0
    while apply_rules(mp) != 0:
        if debug:
            for i in mp:
                for j in i:
                    print(j, end='')
                print()
            print()
        debug_i +=1
        if debug and debug_i == 7:
            exit(1)
        continue
    total = 0
    for i in mp:
        for j in i:
            if j == '#':
                total += 1
    if debug:
        for i in mp:
            print(i)
    return total
'''
Deep copying every iteration is probably not the best approach, but I'm not sure how else to do simultaneous operations
'''
def apply_rules(mp):
    new_mp = copy.deepcopy(mp)
    changes = 0
    for i in range(0, len(mp)):
        for j in range(0, len(mp[i])):
            if mp[i][j] == '.': continue
            occ = 0
            for k in range(8):
                _i, _j = i, j
                #if debug: print('iter start')
                while (_i + di[k] >= 0 and _i + di[k] < len(mp) and _j + dj[k] >= 0 and _j + dj[k] < len(mp[i])):
                    #if debug: print(_i, _j)
                    if new_mp[_i + di[k]][_j + dj[k]] == '#':
                        occ += 1
                        break
                    if new_mp[_i + di[k]][_j + dj[k]] == 'L':
                        break
                    _i += di[k]
                    _j += dj[k]
                #if debug: print('iter end') 
            if mp[i][j] == 'L' and occ == 0: 
                mp[i][j] = '#'
                changes += 1
            elif mp[i][j] == '#' and occ >= 5: 
                mp[i][j] = 'L'
                changes += 1
            
    return changes

print(solve())