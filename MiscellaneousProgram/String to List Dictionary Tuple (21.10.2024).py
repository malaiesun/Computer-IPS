# Program to convert n lines of user input string into list, tuple and dictionary with each word as element 
def getString():
    sr = []
    n = int(input("Enter the number of lines: "))
    for i in range(n):
        print("Enter Line", i+1,":",end = " ")
        sr.extend(input().split())
    return sr

def sliceString(lst):
    tup = tuple(lst)
    dic = {}
    for i in lst:
        dic[len(i)] = i
    return lst, tup, dic

sr = getString()
print(sliceString(sr))
