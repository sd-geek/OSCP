#!/usr/bin/python
import hashlib
for i in range(100):
      file = "shell.php" + str(i)
      hash = hashlib.md5(file.encode())
      dir = hash.hexdigest() + ".php"
      f = open("dict.txt", "a+")
      f.write(dir+"\r\n")
      f.close()
 
