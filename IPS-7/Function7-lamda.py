string1=input()
######################
result = lambda string1:string1[0].lower() in 'aeiou' if string1 else False
print(result(string1)
