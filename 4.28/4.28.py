import random

def leftrotate(x,num):
    return ((x << num) | (x >> (32 - num))) & 0xFFFFFFFF

msg=(b"Hello W1").hex()
key=b"\x8cA\x92E\r\xd48\xc7\xe4U\x92D\x83\x02qq"             #random.randbytes(16)
key_hex=key.hex()
len_data=( len(key_hex) + len(msg) )//2  #do dai data( data = key || msg )
msg+="80"   # them byte 0x80 
len_pad = (56 - (len_data + 1) % 64) % 64 # do dai data < 56 
data= key_hex+ msg + "00" * len_pad  #padding them byte 00 de du 56 byte mod 64
# them 8 byte big edian cuoi cung cho du 64 byte 
# 8 byte big edian = do dai data * 8  
bitlen = len_data * 8
data += f"{bitlen:016x}"
# du 64 byte cho data => chia moi block thanh cac W ( word ), moi W dai 4 byte => moi block co 16 W
W=[]
for i in range (16):
    W.append(int(data[i*8:(i+1)*8],16))
# mo rong thanh 80 W
for i in range (16,80):
    W.append(leftrotate(W[i-3]^W[i-8]^W[i-14]^W[i-16],1))
# 5 hang so cua SHA1
h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0
# nen 80 vong 
a,b,c,d,e=h0,h1,h2,h3,h4
for t in range(80):
    if t <= 19:
        f = (b & c) | ((~b & 0xFFFFFFFF) & d)
        K = 0x5A827999
    elif t <= 39:
        f = b ^ c ^ d
        K = 0x6ED9EBA1
    elif t <= 59:
        f = (b & c) | (b & d) | (c & d)
        K = 0x8F1BBCDC
    else:
        f = b ^ c ^ d
        K = 0xCA62C1D6

    temp = (leftrotate(a, 5) + f + e + K + W[t]) & 0xFFFFFFFF
    e = d
    d = c
    c = leftrotate(b, 30)
    b = a
    a = temp
h0 = (h0 + a) & 0xFFFFFFFF
h1 = (h1 + b) & 0xFFFFFFFF
h2 = (h2 + c) & 0xFFFFFFFF
h3 = (h3 + d) & 0xFFFFFFFF
h4 = (h4 + e) & 0xFFFFFFFF
digest_bytes = (
    h0.to_bytes(4, 'big') +
    h1.to_bytes(4, 'big') +
    h2.to_bytes(4, 'big') +
    h3.to_bytes(4, 'big') +
    h4.to_bytes(4, 'big')
)
digest_hex = ''.join(f'{h:08x}' for h in [h0,h1,h2,h3,h4])
print(digest_hex)
print(key)






