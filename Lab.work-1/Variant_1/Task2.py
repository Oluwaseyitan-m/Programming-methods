# Дана строка. Напишите программу, которая найдет слова по шаблону:
# строка 'ab' повторяется 1 или более раз.

import re

text = 'ab abab ababab aba abb abbb aab abc ab123'
pattern = r'^(?:ab)+$'
result = []
for word in text.split():
    match = re.match(pattern, word)
    if match:
        result += [match.group()]
print(result)