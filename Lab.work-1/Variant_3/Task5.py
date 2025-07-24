# Напишите программу, которая найдет слова следующего вида: по
# краям стоят буквы 'a', а между ними - буква от a до f и от A до Z.

import re

text = 'a0Va abefa abATa adcea aceda aGHMda aza a1a aAa aJA aMa'
pattern = r'\ba[a-fA-Z]*a\b'
print(re.findall(pattern, text))