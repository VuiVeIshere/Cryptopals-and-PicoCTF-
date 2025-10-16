
def blocking(ct : str, block_size = 32):
    ct=ct.strip()
    if len(ct)%32 != 0:
        return []
    return [ct[i:i+block_size] for i in range (0,len(ct),block_size)]

with open('8.txt',"r") as f:
    ct=f.readlines()
repeat_max=-1
best=""
for line in ct:
    blocks=blocking(line,32)
    repeat= len(blocks) -len(set(blocks))
    if repeat>repeat_max:
        repeat_max=repeat
        best=line
print(repeat_max)
print(best)

