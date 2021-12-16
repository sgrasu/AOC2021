from collections import defaultdict

def binaryToBase10(binary: str) -> int:
    res = 0
    for i,b in enumerate(binary[::-1]):
        res += int(b)*(2**i)
    return res

base = defaultdict(lambda: 0)
count = 0

with open('day3.txt', 'r') as file:
    report = file.read().splitlines()
    for line in report:
        count += 1
        for i,b in enumerate(line):
            base[i] += int(b)

    gamma = ''
    epsilon = ''
    for x in sorted(base):
        gamma += str(int(base[x] >= count/2))
        epsilon += str(int(base[x] < count/2))
    
    print(binaryToBase10(gamma)*binaryToBase10(epsilon))