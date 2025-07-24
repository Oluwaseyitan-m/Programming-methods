# Дана строка. Напишите программу, которая найдет слова abba, abbba,
# abbbba и только их.

import re

text = 'aa abba aba abbba abbbba abbaa abbbbba'
pattern = r'\babb+a\b'
result = re.findall(pattern, text)
print(result)