# Дана строка. Напишите программу, которая найдет слова вида aba, в
# которых 'b' встречается менее 3-х раз (включительно).

import re

text = 'aba abba ababa abbba aa abbbba'
pattern = r'\bab{1,3}a\b'
print(re.findall(pattern,text))