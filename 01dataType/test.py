testString = "="*50
print(len(testString))
a = "Life is too short, You need Python"
print(a[13])

string0to4 = a[0:4]
print(string0to4)

stringFrom19 = a[19:]
print("stringFrom19",stringFrom19)

stringTo17 = a[:17]
print("stringTo17",stringTo17)

formatString2 = "I eat %d apples." %3
print("formatString2 :",formatString2)

formatString = "I eat %d apples." 
print(formatString %4)

number = 10
day = "three"
print( "I ate %d apples. so I was sick for %s days." % (number, day))


a = "hobby"
bCountInString= a.count('b')

bIndexinString = a.find('o')

",".join('abcd')
",".join(['a', 'b', 'c', 'd'])

a = "hi"
a.upper()

a = " hi "
a.lstrip()
a.rstrip()

a = "Life is too short"
a.replace("Life", "Your leg")