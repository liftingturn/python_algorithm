num = 1
result = 0
while num<=1000:
    if(num%3==0):
        result += num
    num += 1

count = 0
while count<5:
    count +=1
    print("*"*count)

for num in range(1,101):
    print(num)

points = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for point in points:
    sum += point
average = sum/(len(points))
print(average)


numbers = [1, 2, 3, 4, 5]
result = [num*2 for targetNum in numbers if targetNum % 2 != 0]