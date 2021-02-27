# 대응 관계를 나타내는 자료형을 갖고 있는데, 이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.

# 딕셔너리 요소 삭제하기
del a[1]

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

a.keys()
['name', 'phone', 'birth']

a.values()
['pey', '0119993323', '1118']

a.items()
[('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]

a.clear()
a
{}


a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

print(a.get('nokey'))  #get 으로 가져오면 에러 방지 가능
None

print(a['nokey'])

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'nokey'


# key check
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
'name' in a
True
'email' in a
False