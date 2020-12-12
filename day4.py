def solve(debug=True):
    passports = ['']
    with open('day4.txt', 'r') as f:
        for line in f:
            line = line[:-1] + ' '
            if line.split() == []:
                passports.append('')
            else:
                passports[-1] += line
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #for i in passports:
    #   print(i.split())
    #return 1
    valid = 0
    for passport in passports:
        d = dict()
        passport = passport.split()
        for st in passport: d[st[0:3]] = st
        valid += 1
        for f in fields:
            if f not in d:
                print(f'missing field {f}')
                valid -= 1
                break
            field = d[f]
            val = field[field.find(':')+1:]
            intval = -1000
            try:
                intval = int(val)
            except:
                intval = -1000
            if f == 'byr':
                val = int(val)
                if val < 1920 or val > 2002:
                    if debug: print(f'Field {field} is invalid')
                    valid -= 1
                    break
            elif f == 'iyr':
                val = int(val)
                if val < 2010 or val > 2020:
                    if debug: print(f'Field {field} is invalid')
                    valid -= 1
                    break
            elif f == 'eyr':
                val = int(val)
                if val < 2020 or val > 2030:
                    if debug: print(f'Field {field} is invalid')
                    valid -= 1
                    break
            elif f == 'hgt':
                met = val[-2:]
                if met != 'cm' and met != 'in':
                    if debug: print(f' here Field {field} is invalid')
                    valid -= 1
                    break
                #print(met)
                hgt = int(val[:-2])
                #print(hgt)
                #print(met == 'cm' and (hgt < 150 or hgt > 193))
                if met == 'cm' and (hgt < 150 or hgt > 193):
                    if debug: print(f'Here Field {field} is invalid')
                    valid -= 1
                    break
                elif met == 'in' and (hgt <59 or hgt > 76):
                    if debug: print(f'Field {field} is invalid')
                    valid -= 1
                    break
                #else:
                #    if debug: print(f'Field {field} is invalid')
                #    valid -= 1
                    break   
            elif f == 'hcl':
                res = [val[0] == '#']
                for i in range(1, len(val)):
                    if val[i] in ['0','1','2','3','4','5','6','7','8','9'] or val[i] >= 'a' or val[i] <='f':
                        res.append(True)
                    else:
                        res.append(False)
                if False in res:
                    if debug: print(f'Field {field} is invalid')
                    valid -= 1
                    break
            elif f == 'ecl':
                if val not in ['amb','blu','brn','gry','grn','hzl','oth']:
                    if debug: print(f'Field {field} is invalid')
                    valid -= 1
                    break
            elif f == 'pid':
                if intval == -1000 or len(val) != 9:
                    #print(intval)
                    if debug: print(f'Field {field} is invalid')
                    valid -= 1
                    break

    return valid
print(solve())