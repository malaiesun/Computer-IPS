import re
###################################
st = input()
char1 = input()[0]
char2 = input()[0]

if char1 in st or char2 in st:
    print("match")
else:
    print("no match")

# this method uses the re module
import re
###################################
txt = input()
a = input()[0]
b = input()[0]
x = re.search(r"[a.?b]",txt)
if x:
    print("match")
else:
    print("no match")
