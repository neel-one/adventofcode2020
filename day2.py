
def solve():
    valid = 0
    with open('day2.txt', 'r') as f:
        for line in f:
            hyph = line.find('-')
            sp = line.find(' ')
            col = line.find(':')
            lb = int(line[:hyph])
            ub = int(line[hyph+1:sp])
            letter = line[sp+1]
            password = line[col+2:] 
            num_letter = 0
            for char in password:
                if char == letter:
                    num_letter += 1
            if num_letter >= lb and num_letter <= ub:
                valid += 1
    return valid

def solve2():
    valid = 0
    with open('day2.txt', 'r') as f:
        for line in f:
            hyph = line.find('-')
            sp = line.find(' ')
            col = line.find(':')
            lb = int(line[:hyph])
            ub = int(line[hyph+1:sp])
            letter = line[sp+1]
            password = list(line[col+2:])
            if(lb-1 >= len(password)):
                continue
            elif(ub-1 >= len(password) and password[lb-1] == letter):
                valid += 1
            elif(password[lb-1] == letter or password[ub-1] == letter):
                if(password[lb-1] != password[ub-1]): 
                    valid += 1
            
            
    return valid

print(solve2())
