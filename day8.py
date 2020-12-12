def solve(mem, debug=False):
    '''
    mem = []
    with open('day8.txt', 'r') as f:
        for line in f:
            line = line[:-1]
            mem.append(line)
    '''
    visited = set()
    pc = 0
    acc = 0
    while pc < len(mem):
        if pc in visited: 
            return acc, False
        visited.add(pc)
        instr = mem[pc]
        sp = instr.find(' ')
        op = instr[:sp]
        sign = instr[sp+1]
        num = int(instr[sp+2:])
        if sign == '-': 
            num *= -1
        if op == 'jmp':
            pc += num
            continue
        elif op == 'acc':
            acc += num
        pc += 1
    return acc, True

def solve2():
    mem = []
    with open('day8.txt', 'r') as f:
        for line in f:
            line = line[:-1]
            mem.append(line)
    for i in range(len(mem)):
        instr = mem[i]
        sp = instr.find(' ')
        if instr[:sp] == 'acc':
            continue
        elif instr[:sp] == 'nop':
            new_instr = 'jmp' + instr[sp:]
        elif instr[:sp] == 'jmp':
            new_instr = 'nop' + instr[sp:]
        mem[i] = new_instr
        acc, term = solve(mem)
        if term: 
            return acc
        mem[i] = instr


print(solve2())
