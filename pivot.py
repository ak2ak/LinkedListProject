a = 0x0020
b = str(int(a))
b = b[::-1]
b = int(b)
b = hex(b)
print(hex(a),a,int(b,16),b)