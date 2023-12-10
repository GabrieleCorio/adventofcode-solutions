import re

f = open('input_2.txt', 'r')
f_content = f.read()

digits = []
for line in f_content.split('\n'):
    digit = re.findall(r'\d', line)
    digits.append(int(digit[0]  + digit[-1]))
        
    
print(digits)
print(sum(digits))