strings="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key="ICE"
ans=""
for i in range(len(strings)):
    ans+=chr(ord(strings[i])^ord(key[i%len(key)]))
byte=ans.encode()
print(byte.hex())