# ZAD 1

numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

numbers = [round(num / 10)*10 for num in numbers]

print(numbers)

numbers.sort()
numbers.pop()
del numbers[0]
print(numbers)

sum = 0
for num in numbers: 
    sum += num
mean_number = sum / len(numbers)
print(mean_number)

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

