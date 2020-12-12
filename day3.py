def solve(dj,di):
    print('SOLVING:')
    mp = list()
    with open('day3.txt','r') as f:
        for line in f:
            line = [c for c in line if c != '\n']
            mp.append(line)
    '''
    for i in mp:
        for j in i:
            print(j, end='')
        print()
    '''
    i,j = 0,0
    trees = 0
    while(i < len(mp)):
        #for k in range(4):
            #if mp[i][(j+k) % len(mp[0])] == '#':
            #    trees += 1
        i += di
        j += dj
        
        if i < len(mp):
            if mp[i][j % len(mp[0])] == '#': trees += 1
            #print(i, j % len(mp[0]))
            #print(mp[i][j % len(mp[0])])
            #mp[i][j % len(mp[0])] = 'X'
        #if i == 3:
        #    return trees
    '''
    for i in mp:
        for j in i:
            print(j, end='')
        print()
    '''
    return trees

res = [solve(1,1),solve(3,1),solve(5,1),solve(7,1),solve(1,2)]
tot = 1
for i in res:
    print(i) 
    tot *= i
print(tot)