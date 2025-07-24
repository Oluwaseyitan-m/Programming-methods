# Дана строка. Напишите программу, которая найдет слово a.a, не
# захватив прочие.

import re

text = 'a.a a.ab a.aa a..a a a.a'
pattern = r'\ba\.a\b'
print(re.findall(pattern,text))