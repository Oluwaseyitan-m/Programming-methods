# Дана строка. Напишите программу, которая найдет слова *q+, *qq+,
# *qqq+, не захватив остальные.

import re

text = "*q+ *qq+ *qqq+ *qqqq+ abc *qrs+"
pattern = r'^\*q{1,3}\+$'
result = []
for word in text.split():
    match = re.match(pattern, word)
    if match:
        result += [match.group()]
print(result)