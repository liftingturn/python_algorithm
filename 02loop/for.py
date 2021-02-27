test_list = ['one','two','three']


test_list = ['one', 'two', 'three'] 
for i in test_list: 
     print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
     print(first + last)


add = 0 
for i in range(1, 11):   # js : for(i=1;i<11;i++)
     add = add + i 

for i in range(1,10):
    for j in range(1,10):
        print(f'{i}*{j} = {i*j}', end = " ")
    print('\n')

# List comprehension, js array.map 과 동일
a = [1,2,3,4]
result = [num * 3 for num in a]
result = [num * 3 for num in a if num % 2 == 0]

result = [x*y for x in range(2,10)
              for y in range(1,10)]