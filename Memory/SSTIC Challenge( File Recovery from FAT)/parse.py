from hachoir.parser.misc.ole2 import OLE2_File
from hachoir.stream import FileInputStream

p = OLE2_File(FileInputStream("Recette.doc"))
blocksize = 512
fat = []
for bb in p.array("bbfat"):
    for fld in bb:
        fat.append(fld.value)

# offset from binwalk (+/- 1 to account for 512-byte file header)
start = (0x1E6200 // 512) - 1
chain = [start]
while 1:
    start = fat[start]
    if start > 0xfffffff0:
        break
    chain.append(start)

with open("Recette.doc", "rb") as inf, open("hidden.gz", "wb") as outf:
    for entry in chain:
        inf.seek((entry + 1) * 512)
        outf.write(inf.read(512))
