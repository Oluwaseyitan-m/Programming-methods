# Напишите программу, которая найдет слова следующего вида:
# по краям стоят буквы 'a', а между ними - буква от a до g.

# a-g: a, b, c, d, e, f, g

import re

text = 'abcda adeba abec aa afwta adnea'
pattern = r'^a[b-g]*a\b$'
result = []
for word in text.split():
    match = re.match(pattern, word)
    if match:
        result += [match.group()]
print(result)