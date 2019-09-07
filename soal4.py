import re

def groupNumber(x):
    x = re.sub(r'\D', '', x)
    x = [x[i:i+3] for i in range(0, len(x), 3)]
    if len(x[-1]) == 1:
      x[-2], x[-1] = x[-2][:-1], x[-2][-1] + x[-1]
    return print('-'.join(x))

x='1213123 asdasd 12312 3121 '
groupNumber(x)
