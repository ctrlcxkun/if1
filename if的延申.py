age = input('禁止未成年进入网吧请输入你的年龄: ')
age = int(age)
if age <= 18:
	print('未成年禁止进入网吧')
else:
	print('你可以正常上网啦')