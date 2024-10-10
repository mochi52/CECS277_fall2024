def read_map():
    file = open("map.txt")
    map2d = []
    
    for row in file:
        sublist = []
        for e in row:
            if e != ' ' and e != '\n':
                sublist.append(e)
        map2d.append(sublist)
        
    return map2d

def main():
    map = read_map()
    print(map)

main()
