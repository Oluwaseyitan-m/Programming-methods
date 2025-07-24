# Дана строка. Напишите программу, которая найдет слова,
# в которых по краям стоят буквы 'a', а между ними любое количество цифр
# (в том числе и ноль цифр, то есть строка 'aa').

import re

text = 'a12a a451a a152b aa abba a8a'
pattern = r'^a\d*a$'
result = []
for word in text.split():
    match = re.match(pattern, word)
    if match:
        result += [match.group()]
print(result)