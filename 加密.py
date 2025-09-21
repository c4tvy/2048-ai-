def chinese_to_unicode(text):
    return ''.join([f'{ord(char):04x}' for char in text])
a=input("请输入要加密的内容")
a=(chinese_to_unicode(a))
d=""
for b in a:
    c = format(int(b, 16), '0{}b'.format(len(b)*4))
    d=d+str(c)
f=""
for e in str(d):
    if e=="0":
        f=f+"⬛"
    if e =="1":
        f=f+"⬜"
f=f[::-1]
print(f)