

try:
   f = open(r"C:\Users\SUMANTH\Desktop\sample.txt")
   #C:\Users\SUMANTH\Desktop\sample.txt

   content = f.read()
   print(content)

   f1 = open(r"C:\Users\SUMANTH\Desktop\sample_write123.txt",mode="w+")
   f1.write(content)
   # perform file operations

except:
   print("That's a nonsense path man!!")
finally:
   print("closing the files..")
   f.close()
   f1.close()