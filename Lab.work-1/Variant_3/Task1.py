# Дана строка. Напишите программу, которая найдет слова abba и abea,
# не захватив прочие.

import re

text = 'abba aba abbba abea abbabba abbea abea'
pattern = r'\bab[be]a\b'
result = re.findall(pattern, text)
print(result)