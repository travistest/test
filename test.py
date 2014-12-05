a = input('Введите а:')
b = input('Введите b:')
c = input('Введите c:')
if len(a) > 0 and len(b) > 0 and len(c) > 0 and not a.isalpha() and not b.isalpha() and not c.isalpha():
	d = int(b) ** 2 - 4 * int(a) * int(c)
	if d > 0 or d == 0:
		import math
		dd = math.sqrt(d)
		x = ( -int(b) - int(dd) ) / (int(a) * 2)
		x1 = ( -int(b) + int(dd) ) / (int(a) * 2)
		print (x, x1)
	else:
		print ('Рещений не имеет')
else:
	print ('Введите только числа')
