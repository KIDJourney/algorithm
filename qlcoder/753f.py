f = open('144043063958496.txt' , 'r')

lines = f.readlines()

priceDir = {i:0 for i in range(100000)}

ans = 0

for line in lines:
    line = line.split()
    line = [line[0] , int(line[1]) , int(line[2])]
    if line[0] == 'up':
        priceDir[line[2]] += line[1]

    if line[0] == 'query':
        ans += sum(priceDir[i] for i in range(line[1] , line[2] + 1))

    if line[0] == 'down':
        priceDir[line[2]] -= line[1]

print(ans) 