def eating(socks: list):
    count = {}
    
    for sock in socks:
        if sock in count:
            count[sock] += 1
        else:
            count[sock] = 1
    
    #missing socks
    missing = 0
    for i in count.values():
        if i % 2 != 0:
            missing += 1
    
    return missing 

input()
socks = list(map(int, input().split()))
print(eating(socks))