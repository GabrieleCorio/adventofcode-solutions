import re

f = open('input.txt', 'r')
f_content = f.read()

compatible_round = []
for line in f_content.split("\n"):
    
    game_datas = line.split(': ')
    ok = True

    for round in game_datas[1].split('; '):
        
        red, blue, green = 0, 0, 0
        for extraction in round.split(', '):

            if extraction.endswith(' red'):
                red = int(extraction.replace(' red', ''))
            
            if extraction.endswith(' blue'):
                blue = int(extraction.replace(' blue', ''))

            if extraction.endswith(' green'):
                green = int(extraction.replace(' green', ''))
        
        
        if red > 12 or blue > 14 or green > 13:
            ok = False 
        
    if ok:
        compatible_round.append(int(game_datas[0].replace('Game ', '')))
        continue
    
    
            

print(sum(compatible_round))


    