types = set()

table = {}

codes = open('codes.txt' , 'r').readlines()

for code in codes :
    code = code.strip().split()
    print(code)
    if code[0] == 'type' and code[1] not in types:
        types.add(code[1])
        continue
    if code[1] == ':=' and code[0] not in table :
        if code[2] == 'new' :
            if code[3] in types:
                table[code[0]] = code[3]
                continue
        else :
            if code[2] in table :
                table[code[0]] = table[code[2]]
                continue



print('-'.join([i[0] + '-' + i[1] for i in sorted(table.items(), key=lambda x : x[0])]))
