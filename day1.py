
def didIncrease(a: float ,b: float) -> bool:
    return b > a

increase_count = 0

with open('day1.txt','r') as file:
    lines = list(map(float,file.read().splitlines()))
    for i in range(1,len(lines)):
        increase_count += didIncrease(lines[i-1],lines[i])
    
    print(increase_count)
    increase_count = 0

    for i in range(0,len(lines)-2):
        increase_count += didIncrease(sum(lines[i:(i+3)]), sum(lines[(i+1):(i+3+1)]))

    print(increase_count)