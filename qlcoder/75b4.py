string = """^BABABABANANABABABABABANANABABABABABANANABANANANAAHH|"""

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character,count)
        lst.append(entry)
    return lst
    
stringList = []
stringLen = len(string)

for i in range(stringLen):
    stringList.append("{0}{1}".format(string[stringLen-i:] , string[:stringLen-i]))

stringList = sorted(stringList)

after = ''.join([i[-1] for i in stringList])

after = encode(after)
print(''.join(["{0}{1}".format(item[0],item[1]) for item in after]))