a = [1,2,3]
b = a

id(a)
4303029896
id(b)
4303029896

a is b  # a와 b가 가리키는 객체는 동일한가?
True

# 그렇다면 b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만들수는 없을까? 다음 2가지 방법이 있다.

a = [1, 2, 3]
b = a[:]
a[1] = 4
a
[1, 4, 3]
b
[1, 2, 3]

from copy import copy
b = copy(a)


[a,b] = ['python', 'life']
# 또한 여러 개의 변수에 같은 값을 대입할 수도 있다.

a = b = 'python'

a = 3
b = 5
a, b = b, a
a
5
b
3