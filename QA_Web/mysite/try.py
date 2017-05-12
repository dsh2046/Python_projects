import re
from collections import Counter


x = '1234567890'
com = re.compile(r'((?<=\d)\d{3})')
data = com.findall(x)
print data
