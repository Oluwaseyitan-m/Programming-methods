# Дана строка. Напишите программу, которая найдет слова вида:
# по краям стоят буквы 'a' и 'b', а между ними - не буква и не цифра.

import re

text = 'a!b a?b a1b a-b a+b a=b a#b a.b a\nb axb aWb'
pattern =  r'\ba\Wb\b'
print(re.findall(pattern,text))