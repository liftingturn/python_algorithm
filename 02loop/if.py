money = True
if money :
    print("ride taxi")
else:
    print("walk")

if money:
    print('ride')
    print('txi')
    print('taxi')


# 비교연산자	설명
# x < y	x가 y보다 작다
# x > y	x가 y보다 크다
# x == y	x와 y가 같다
# x != y	x와 y가 같지 않다
# x >= y	x가 y보다 크거나 같다
# x <= y	x가 y보다 작거나 같다

# 연산자	설명
x or y	#x와 y 둘중에 하나만 참이어도 참이다
x and y	#x와 y 모두 참이어야 참이다
not x	#x가 거짓이면 참이다

money = 2000
card = True
if money>=3000 or card:
    print('taxi')
else:
    print('walk')

1 in [1,2,3]
4 not in [1,2,3]

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")