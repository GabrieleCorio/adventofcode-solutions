import re

f = open('input.txt', 'r')
f_content = f.read()

mulTot = []
for line in f_content.split("\n"):
    
    game_datas = line.split(': ')

    red, blue, green = 0, 0, 0
    for round in game_datas[1].split('; '):
        
        
        for extraction in round.split(', '):

            if extraction.endswith(' red'):
                redNew = int(extraction.replace(' red', ''))
                
                if red < redNew:
                    red = redNew
                
            
            if extraction.endswith(' blue'):
                blueNew = int(extraction.replace(' blue', ''))

                if blue < blueNew:
                    blue = blueNew

            if extraction.endswith(' green'):
                greenNew = int(extraction.replace(' green', ''))

                if green < greenNew:
                    green = greenNew
    
    mul = 1

    if red != 0:
        mul *= red

    if blue != 0:
        mul *= blue

    if green != 0:
        mul *= green

    mulTot.append(mul)

print(sum(mulTot))


    