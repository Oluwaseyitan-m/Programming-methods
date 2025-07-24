# Дана строка. Напишите программу, которая найдет слова aa, aba, abba,
# abbba и т.д., не захватив остальные.

import re

text = 'aa abab aba abba abbaa abbba abbbbba'
pattern = r'^a[b]+a$'
result = []
for word in text.split():
    match = re.match(pattern, word)
    if match:
        result += [match.group()]
print(result)

