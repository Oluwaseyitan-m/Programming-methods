# Дана строка. Напишите программу, которая найдет слова ahb, acb,
# aeb по шаблону, а остальные слова проигнорирует.

import re

text = 'ahb acb aeb aef aghb aijb'
pattern = r'^a[hce]b\b$'
result = []
for word in text.split():
    match = re.match(pattern, word)
    if match:
        result += [match.group()]
print(result)
