import re

p = r'^[a-zA-Z0-9._%+-]+@[a-z]+\.com$'
r =re.match(p,'xyz@gmail.com')
print(r.group())

import re

pattern = r'^(?=.*[a-z])$'
tests = ['98', '242526', '1234567890']

for num in tests:
    if re.findall(pattern, num):
        print(num, "valid")
    else:
        print(num, "non valid")
