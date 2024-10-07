import re

n = int(input())
strings = []
for i in range(n):
    s = input()
    strings.append(s)


print(strings)

for string in strings:
    if re.findall(r"do*$", string):
        print("match found for pattern1")
    else:
        print("No match found for pattern1")
        
for string in strings:    
    if re.findall(r"do?", string):
        print("match found for pattern2")
    else:
        print("No match found for pattern2")
        
for string in strings:   
    if re.findall(r"do{2}", string):
        print("match found for pattern3")
    else:
        print("No match found for pattern3")
