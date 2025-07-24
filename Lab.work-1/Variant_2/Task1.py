# Дана строка. Напишите программу, которая найдет слова abba, adca,
# abea по шаблону, а остальные слова проигнорирует.

import re

text = 'abba adca abe abea abbaa adcafg'
pattern = r'^a[b-e]*a\b$'
result = []
for word in text.split():
    match = re.match(pattern, word)
    if match:
        result += [match.group()]
print(result)