strings="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
frequen="ETAOINSHRDLCUMWFGYPBVKJXQZ"
frequen=frequen[::-1]
def scorechar(s:bytes)->int:
    score=0
    for byte in s:
        ch=chr(byte)
        ch=ch.upper()
        if byte<32 or byte>126:
            score-=5
        if ch in frequen:
            score+=frequen.index(ch)
        if ch == 'Z':
            score+=1
        if ch == ' ':
            score+=5
    return score

best=0
for i in range(256):
    xor=bytes(i^k for k in bytes.fromhex(strings))
    score=scorechar(xor)
    if score>best:
        best=score
        beststr=xor
print(beststr.decode())

