def convert(number):  
################################
    print(bin(number))
    print(oct(number))
    print(hex(number))
    for i in range(number + 1):
        if i in [2,3,5,7]:
            print(i)
        elif i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0 or i == 1:
            pass
        else:
            print(i)

import re
s1 = "Please Plant More Trees"
x = re.findall("\S",s1)
###################################
n=int(input())
convert(n)
