a=open("a","r").read()
b=open("b","r").read()

text=""
arr=a.split("\n")
for i in arr:
   if i.count(".") != 3:
      continue
   I=i.split(".")
   text=text + ''.join([chr(int(char)) for char in I])

print(text)

text=""

arr=b.split("\n")
for i in arr:
   if i.count(".") != 3:
      continue
   I=i.split(".")
   text=text + ''.join([chr(int(char)) for char in I])

print(text)


