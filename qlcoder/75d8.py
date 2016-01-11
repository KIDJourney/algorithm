from operator import add
lifes = [(0,1),(0,2),(1,0),(1,1),(2,1)]

max_life = 0
path = ""

poses = [(0,1) , (1,0) , (0,-1) , (-1,0) , (1,1) , (-1,1) , (-1,-1) , (1,-1)]


pro = len(lifes)


for i in range(1000):
    path += str(len(lifes)) + '-'

    temp_map = {}

    for life in lifes:
        temp_pos = [tuple(map(add , life , pos)) for pos in poses]
        for pos in temp_pos:
            temp_map.setdefault(pos,0)
            temp_map[pos] += 1

    for pos in list(temp_map.keys()):
        if pos in lifes :
            if temp_map[pos] < 2 :
                del temp_map[pos]
            elif temp_map[pos] > 3 :
                del temp_map[pos]
        elif temp_map[pos] != 3:
                del temp_map[pos]
    lifes = temp_map.keys()

print(path)