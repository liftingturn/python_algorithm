def add(a,b):
    return a+b

# 람다표현식 : 정렬함수 혹은 콜백용도로 많이 사용
(lambda a,b:a+b)(3,7)

def my_key(x):
    return x[1]

array = [('아무개',50),('아무개',32),('아무개',74)]
print(sorted(array,key=my_key))

print(sorted(array,key=lambda x:x[1]))

#여러개 리스트 대상일때
list1 = [1,2,3,4]
list2 = [1,2,3,4]
result = map(lambda a,b : a+b,list1,list2)
