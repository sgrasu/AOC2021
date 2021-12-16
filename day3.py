from collections import defaultdict

def binaryToBase10(binary: str) -> int:
    res = 0
    for i,b in enumerate(binary[::-1]):
        res += int(b)*(2**i)
    return res

base = defaultdict(lambda: 0)
count = 0

treeDictionary = dict()
treeCount = defaultdict(lambda: 0)

with open('day3.txt', 'r') as file:
    report = file.read().splitlines()
    for line in report:
        count += 1
        for i,b in enumerate(line):
            base[i] += int(b)
            treeDictionary[line[:(i+1)]] = line
            treeCount[line[:(i+1)]] += 1

    gamma = ''
    epsilon = ''
    for x in sorted(base):
        gamma += str(int(base[x] >= count/2))
        epsilon += str(int(base[x] < count/2))
    
    print(binaryToBase10(gamma)*binaryToBase10(epsilon))

    oxygenKey = ''
    while treeCount[oxygenKey] > 1 or oxygenKey == '':
        oxygenKey += '0'
        oxygenKeyFlip = oxygenKey[:-1] + '1'
        print(f'{oxygenKey}: {treeCount[oxygenKey]} <=> {oxygenKeyFlip}: {treeCount[oxygenKeyFlip]}')
        oxygenKey = oxygenKey if treeCount[oxygenKey] > treeCount[oxygenKeyFlip] else oxygenKeyFlip
    
    oxygenValue = binaryToBase10(treeDictionary[oxygenKey])
    print(f'{treeDictionary[oxygenKey]} = {oxygenValue}')

    c02Key = ''
    while treeCount[c02Key] > 1  or c02Key == '':
        c02Key += '0'
        c02KeyFlip = c02Key[:-1] + '1'
        print(f'{c02Key}: {treeCount[c02Key]} <=> {c02KeyFlip}: {treeCount[c02KeyFlip]}')
        c02Key = c02Key if treeCount[c02Key] <= treeCount[c02KeyFlip] else c02KeyFlip
    
    c02Value = binaryToBase10(treeDictionary[c02Key])
    print(f'{treeDictionary[c02Key]} = {c02Value}')

    print(oxygenValue*c02Value)
        