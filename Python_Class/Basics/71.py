import re

results = re.match(r'\d', "123")
print(results.group())

results = re.search(r'\w', "abc223")
print(results.group())

results = re.split(r'[,:]', "awd:,awd")
print(results)

results = re.split(r'[,:]', "awd:,awd")
print(results)

results = re.search(r'\d{2}-\d{4}', "12-3455")
print(results.group())

results = re.sub(r'(\d{2})-(\d{4})', r'xx-xxxx-\2', "abc-12-2345")
print(results)

import re

text='2024-12-28'

result= re.search(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',text)

print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))
print(result.group('year'))
print(result.group('month'))
print(result.group('day'))
print(result.groupdict())


text1="John Smith"

pattern1=r'(?P<first>\w+) (?P<last>\w+)'
replace1=r'\g<last>,\g<first>'

result=re.sub(pattern1,replace1,text1)
print(result)


text1="John Smith"

pattern1=r'(?P<first>\w+) (?P<last>\w+)'
replace1=r'\g<last>,\g<first>'

result=re.sub(pattern1,replace1,text1)
print(result)

import re
text= "this is Is a text text"

pattern=r'(\b\w+\b)\s+\1'

duplicates=re.findall(pattern,text,flags=re.I)

print(duplicates)


import re

text = "my phone number are 12344 and 6537378"
pattern= r'\d+'

matches = re.finditer(pattern,text)

for match in matches:
    print("match:", match.group(), "start:", match.start(), "end:", match.end())

nums= ['9887723823', '9870878876', '912', '1982398012897123']
p = r'^[0-9]{10}$'
for n in nums:
    if re.match(p,n):
        print(n,"valid")

    else:
        print(n,"invalid")
