# Дана строка. Напишите программу, которая найдет слова следующего вида:
# по краям стоят буквы 'a' и 'b', а между ними - не число.

import re

text = 'aXb a4b a_b a-b a+b a b axb a123b'
pattern = r'\ba\Db\b'
result = re.findall(pattern, text)
print(result)
