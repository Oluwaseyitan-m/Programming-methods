# Напишите программу, которая найдет слова следующего вида: по
# краям стоят буквы 'a', а между ними - буква от a до f или от j до z.

# a-f: a,b,c,d,e,f
# j-z: j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z

import re

text = 'abcda ajnowa agia aopbea ayzxa aba aca aha aga aea aja'
pattern = r'\ba[a-fj-z]+a\b'
result = re.findall(pattern, text)
print(result)
