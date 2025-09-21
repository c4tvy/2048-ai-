a=input("请输入要解密的内容")
a=a[::-1]
c=""
f=""
for b in str(a):
    if b =="⬛":
        c=c+"0"
    if b =="⬜":
        c=c+"1"
for d in range(int(len(c)/16)):
    e=chr(int(c[d*16:d*16+16],2))
    f=f+e
print(f)