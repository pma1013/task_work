import re

S = input().rstrip()
R = input().rstrip()

pattern = re.compile(R)
m_obj = pattern.match(S)

print(len(m_obj.group())

