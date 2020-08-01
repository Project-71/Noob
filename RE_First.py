import re

pattern_obj = re.compile('(\d+)(\w+)')
res = re.match(pattern_obj,'123456abcefg')
print(res)
print(res.group(1))
print(res.group(2))

pattern_obj = re.compile('(x.)')
res = re.match(pattern_obj,'xc,dq,eq')
print('\n',res.group(1))

pattern_obj = re.compile('(a*)')
res = re.match(pattern_obj,'aa123456aabcefg')
print('\n',res.group(1))

pattern_obj = re.compile('(A?\w\w)')
res = re.match(pattern_obj,'AccBB')
print('\n',res.group(1))

pattern_obj = re.compile('(a+)')
res = re.match(pattern_obj,'aaabcj')
print('\n',res.group(1))

pattern_obj=re.compile('(^ab)')
res=re.match(pattern_obj,'abcdef')
print('\n',res.group(1))

pattern_obj=re.compile('(a$)')
res=re.match(pattern_obj,'a')
print('\n',res.group(1))

pattern_obj=re.compile('(x.*x)')
res=re.match(pattern_obj,'xTsaaaaaadx')
print('\n',res.group(1))

pattern_obj=re.compile('(a.*?b)')
res=re.match(pattern_obj,'aljlkjjljljdebfkknkhkhkhlkb')
print('\n',res.group(1))

pattern_obj=re.compile('(a.+b)')
res=re.match(pattern_obj,'adaewawaab')
print('\n',res.group(1))

pattern_obj=re.compile('((heihei|haha)123)')
res=re.match(pattern_obj,'heihei123')
print('\n',res.group(1))
print(res.group(2))
