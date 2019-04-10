import re
matcher=re.finditer('a?','anappleisapple')
for m in matcher:
    print(m.start(),'..',m.group())
    
