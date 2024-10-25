  # 1.CREATE A FILE AND WRITE MULTIPLE LINES INTO THE FILES
  # 2.READ THE CONTENTS OF THE FILE 
  # 3.READ A SINGLE LINE THE FILE
  # 4.MAKE USE OF WRITE,WRITELINES,READ,READLINES
  with open('something.txt','w') as file:
      file.writelines(["First line.\n", "Second line.\n", "Third line.\n"])
  
  with open('example.txt', 'r') as file:
      content = file.read()
      print(content)
 
  with open('example.txt', 'r') as file:
      single_line = file.readline()
       print(single_line)
   
   with open('example.txt', 'a') as file:
       file.write("Fourth line.\n")
   
   with open('example.txt', 'r') as file:
       lines = file.readlines()
       for line in lines:
            print(line.strip())                                 
