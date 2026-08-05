import re
value = input()
split = value.split(',')
result = re.findall('\d+', value)
t = tuple(result)
print(result)
print(t)
