import re


test1 = "snake_people"
x = re.sub(r'_([\w])', lambda x: x.group(1).upper(), test1)
print(x)