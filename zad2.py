# ZAD 2

def build_bridge(chunk,goal):
    flag = True
    while goal > 0:
        goal -= chunk
        if goal <= 0:
            flag = True
            break 
        goal -= chunk/2
        flag = False     
    return flag


print(build_bridge(2,20))
print(build_bridge(2,18))
